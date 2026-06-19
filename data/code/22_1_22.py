class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [1, 2, 3, 4, 5]
    results = {num: checker.check_odd(num) for num in sample_values}
    print(results)