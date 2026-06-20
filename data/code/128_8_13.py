class NumberChecker:
    NEGATIVE = -1

    @staticmethod
    def check_negativity(value):
        return value < 0

if __name__ == '__main__':
    numbers_to_check = [10, -5, 20, -1, 33, -12, 0]
    for number in numbers_to_check:
        result = NumberChecker.check_negativity(number)
        print(f"Number: {number}, Negative: {result}")