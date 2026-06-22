class NumberSequence:
    START = 1
    END = 50

    @staticmethod
    def generate_sequence():
        return [i for i in range(NumberSequence.START, NumberSequence.END + 1)]

if __name__ == '__main__':
    sequence = NumberSequence.generate_sequence()
    for number in sequence:
        print(number)