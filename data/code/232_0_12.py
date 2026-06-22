class NumberSequence:
    MAX_NUMBER = 50

    @staticmethod
    def generate_sequence():
        return [i for i in range(1, NumberSequence.MAX_NUMBER + 1)]

if __name__ == '__main__':
    sequence = NumberSequence.generate_sequence()
    for number in sequence:
        print(number)