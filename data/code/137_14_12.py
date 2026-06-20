class NumberChecker:
    @staticmethod
    def is_even(number):
        return (number & 1) == 0

if __name__ == '__main__':
    test_numbers = [2, 3, 4, -6, -7]
    for num in test_numbers:
        print(f"Number {num} is even: {NumberChecker.is_even(num)}")