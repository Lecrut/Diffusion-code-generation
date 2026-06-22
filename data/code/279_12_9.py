class EvenNumberPrinter:
    START = 0
    END = 99

    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @classmethod
    def print_evens(cls):
        for num in range(cls.START, cls.END + 1):
            if cls.is_even(num):
                print(num)

if __name__ == '__main__':
    EvenNumberPrinter.print_evens()