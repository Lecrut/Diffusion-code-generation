class NumberChecker:
    def is_negative(self, number):
        return number < 0

if __name__ == '__main__':
    checker = NumberChecker()
    test_numbers = [10, -5, 0, -100, 3.14]
    for num in test_numbers:
        result = checker.is_negative(num)
        print(f"Testing number: {num}, Is negative: {result}")