class SequenceRepeater:
    REPEAT_COUNT = 5

    @staticmethod
    def perform_action():
        print("Action repeated")

    @classmethod
    def repeat_sequence(cls):
        for _ in range(cls.REPEAT_COUNT):
            cls.perform_action()

if __name__ == '__main__':
    SequenceRepeater.repeat_sequence()