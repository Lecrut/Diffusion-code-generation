class NumberChecker:
    def check_odd(self, number):
        is_odd = (number % 2 != 0)
        return is_odd

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [10, 15, -2, 7, -8]
    results = [checker.check_odd(value) for value in sample_values]
    print(results)