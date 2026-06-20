class NegativeChecker:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    test_cases = [10, -5, 0, -100, 3.14, -1.5]
    for case in test_cases:
        print(f"The number {case} is {'negative' if NegativeChecker.is_negative(case) else 'not negative'}.")