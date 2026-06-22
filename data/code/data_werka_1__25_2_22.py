class ValueChecker:
    def check_if_zero(self, value):
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    sample_values = [0, 1, -1, 2.5, None, '']
    for value in sample_values:
        print(f"Is {value} zero? {checker.check_if_zero(value)}")