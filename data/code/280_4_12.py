class SquarePrinter:
    MAX_REPETITIONS = 20

    @staticmethod
    def print_squares(times):
        if times != SquarePrinter.MAX_REPETITIONS:
            raise ValueError('Repetitions must be exactly 20.')
        for i in range(1, times + 1):
            print(i ** 2)

if __name__ == '__main__':
    try:
        repetitions = SquarePrinter.MAX_REPETITIONS
        SquarePrinter.print_squares(repetitions)
    except Exception as e:
        print(f'An error occurred: {e}')