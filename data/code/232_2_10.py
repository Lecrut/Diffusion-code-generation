import itertools

class NumberSequence:
    START = 1
    COUNT = 20

    @staticmethod
    def print_sequence():
        for number in itertools.count(start=NumberSequence.START):
            if number > NumberSequence.COUNT:
                break
            print(number)

if __name__ == '__main__':
    NumberSequence.print_sequence()