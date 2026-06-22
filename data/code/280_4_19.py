class SquarePrinter:
    MAX_REPETITIONS = 20

    @staticmethod
    def print_square(number):
        print(f'{number} squared is {number ** 2}')

    @classmethod
    def repeat_action(cls, times=MAX_REPETITIONS):
        for i in range(1, times + 1):
            cls.print_square(i)

if __name__ == '__main__':
    SquarePrinter.repeat_action()