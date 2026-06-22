class NumberChecker:
    def check_positivity(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or float")
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = {
        "positive_integer": 15,
        "negative_integer": -7,
        "zero": 0,
        "positive_float": 2.718,
        "negative_float": -3.14
    }
    results = {key: checker.check_positivity(value) for key, value in sample_values.items()}
    print(results)