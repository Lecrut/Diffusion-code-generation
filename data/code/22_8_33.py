class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    test_cases = [4, 7, 0, -3, -4]
    for num in test_cases:
        print(f"{num} is odd: {checker.check_odd(num)}")