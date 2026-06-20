class ZeroChecker:
    @staticmethod
    def is_zero(value):
        return value == 0

if __name__ == '__main__':
    checker = ZeroChecker()
    sample_values = [0, 5, -3, 0.0, 100]
    for value in sample_values:
        result = checker.is_zero(value)
        print(f"Value: {value}, Is Zero: {result}")