class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    test_number = 7
    is_odd_result = checker.check_odd(test_number)
    print(f"The number {test_number} is odd: {is_odd_result}")