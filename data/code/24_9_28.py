class NumberChecker:
    def check_negativity(self, value):
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10, -5, 0, -3.14, 20]
    results = {value: checker.check_negativity(value) for value in sample_values}
    print(results)