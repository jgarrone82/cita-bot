import os
from shutil import which


class eSpeakSpeaker:
    @classmethod
    def is_applicable(cls):
        return which("espeak") is not None

    def say(self, phrase):
        os.system("espeak '" + phrase + "'")


class saySpeaker:
    @classmethod
    def is_applicable(cls):
        return which("say") is not None

    def say(self, phrase):
        os.system("say '" + phrase + "'")


class wSaySpeaker:
    @classmethod
    def is_applicable(cls):
        return which("wsay") is not None

    def say(self, phrase):
        os.system('wsay "' + phrase + '"')


class NullSpeaker:
    """Fallback when no TTS engine is found: prints instead of crashing on import."""

    def say(self, phrase):
        print(f"[SPEAKER] {phrase}")


def new_speaker():
    for cls in [eSpeakSpeaker, saySpeaker, wSaySpeaker]:
        if cls.is_applicable():
            return cls()
    print("WARNING: no TTS engine (espeak/say/wsay) found. Install wsay on Windows for voice alerts.")
    return NullSpeaker()
