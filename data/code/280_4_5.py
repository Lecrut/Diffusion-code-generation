class SquarePrinter:
    MAX_REPETITIONS = 20

    @staticmethod
    def print_square(number):
        print(f'Square of {number}: {number ** 2}')

    @classmethod
    def repeat_action(cls, times=MAX_REPETITIONS):
        if times != cls.MAX_REPETITIONS:
            raise ValueError('Repetitions must be exactly 20.')
        for i in range(1, times + 1):
            cls.print_square(i)

if __name__ == '__main__':
    try:
        SquarePrinter.repeat_action()
    except Exception as e:
        print(f'An error occurred: {e}')