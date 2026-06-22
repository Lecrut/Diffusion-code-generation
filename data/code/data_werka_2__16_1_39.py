class NumberChecker:
    def check_positivity(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or float")
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [15, -7, 0, 2.8, -3.6]
    for value in sample_values:
        result = checker.check_positivity(value)
        print(f"Value: {value}, Is Positive: {result}")