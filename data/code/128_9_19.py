class NegativeChecker:
    @staticmethod
    def is_negative(value):
        return value < 0

if __name__ == '__main__':
    checker = NegativeChecker()
    test_values = [-10, 5, 0, -3, 2]
    for val in test_values:
        print(f"Value {val} is negative: {checker.is_negative(val)}")