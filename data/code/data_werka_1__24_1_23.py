class NumberChecker:
    def check_if_negative(self, value):
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10, -5, 0, -3.5]
    results = {value: checker.check_if_negative(value) for value in sample_values}
    print(results)