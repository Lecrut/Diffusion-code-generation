class RangeCycler:
    START = 100
    END = 200

    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @classmethod
    def cycle_and_print_evens(cls):
        for num in range(cls.START, cls.END + 1):
            if cls.is_even(num):
                print(num)

if __name__ == '__main__':
    RangeCycler.cycle_and_print_evens()