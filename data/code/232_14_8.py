class NumberSequence:
    MAX_ITERATIONS = 5

    @staticmethod
    def print_sequence():
        for i in range(1, NumberSequence.MAX_ITERATIONS + 1):
            print(i ** 2)

if __name__ == '__main__':
    NumberSequence.print_sequence()