import itertools

class SequencePrinter:
    DEFAULT_COUNT = 20
    START_VALUE = 1
    
    @staticmethod
    def print_sequence(count=DEFAULT_COUNT, start=START_VALUE):
        for number in itertools.count(start=start):
            if number > count:
                break
            print(number)

if __name__ == '__main__':
    SequencePrinter.print_sequence()