class NumberChecker:
    def check_odd(self, number):
        return True if number % 2 != 0 else False

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [7, 8, 9, 10, 11]
    results = {value: checker.check_odd(value) for value in sample_values}
    for value, is_odd in results.items():
        print(f"{value} is odd: {is_odd}")