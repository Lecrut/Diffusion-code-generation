class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [1, 2, 3, 4, 5]
    results = {value: checker.check_odd(value) for value in sample_values}
    print(results)