class ValueChecker:
    def check_for_zero(self, value: int | float) -> bool:
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 0.0, 0.1]
    for value in sample_values:
        print(f"Is {value} zero? {checker.check_for_zero(value)}")