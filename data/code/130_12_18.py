class ZeroChecker:
    @staticmethod
    def is_zero(value: int) -> bool:
        return value == 0

if __name__ == '__main__':
    checker = ZeroChecker()
    sample_values = [10, 0, -5, 0, 3.14]
    for value in sample_values:
        result = checker.is_zero(value)
        print(f"Checking value: {value}, Result: {result}")