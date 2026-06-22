import time

class SequenceRepeater:
    DELAY_SECONDS = 1

    @staticmethod
    def perform_action():
        print('Action executed')

    @classmethod
    def repeat_sequence(cls):
        for _ in range(3):
            cls.perform_action()
            time.sleep(cls.DELAY_SECONDS)

if __name__ == '__main__':
    SequenceRepeater.repeat_sequence()