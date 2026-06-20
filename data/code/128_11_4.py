class NumberChecker:
    def is_negative(self, number):
        return number < 0

if __name__ == '__main__':
    checker = NumberChecker()
    test_cases = [-5.0, 0, 3.14]
    for case in test_cases:
        print(checker.is_negative(case))