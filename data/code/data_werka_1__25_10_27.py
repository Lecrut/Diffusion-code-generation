class ValueChecker:
    def check_for_zero(self, value: int) -> bool:
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 100, -100]
    for value in sample_values:
        result = checker.check_for_zero(value)
        print(f"Is {value} zero? {result}")