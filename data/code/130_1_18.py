class ZeroChecker:
    def is_zero(self, number):
        return not number

if __name__ == '__main__':
    checker = ZeroChecker()
    sample_values = [0, 5, -3, 0.0]
    for value in sample_values:
        result = checker.is_zero(value)
        print(f"Checking value: {value}, Is zero: {result}")