class SequenceRepeater:
    GREETING = 'Hello'
    ADDITION = 2 + 3
    MULTIPLICATION_FACTOR = 4

    @staticmethod
    def repeat_sequence():
        for _ in range(3):
            print(SequenceRepeater.GREETING)
            result = (SequenceRepeater.ADDITION) * SequenceRepeater.MULTIPLICATION_FACTOR
            print(result)

if __name__ == '__main__':
    SequenceRepeater.repeat_sequence()