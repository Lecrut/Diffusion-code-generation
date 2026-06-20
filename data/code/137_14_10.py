class NumberChecker:
    def is_even(self, number):
        return number & 1 == 0

if __name__ == '__main__':
    checker = NumberChecker()
    test_numbers = [2, 3, 4, -6, -7]
    for num in test_numbers:
        print(f"Number {num} is even: {checker.is_even(num)}")