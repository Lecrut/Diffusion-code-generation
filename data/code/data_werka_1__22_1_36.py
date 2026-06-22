class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    samples = [15, -2, 8, 7, 0]
    checker = NumberChecker()
    for sample in samples:
        result = checker.check_odd(sample)
        print(f"{sample} is odd: {result}")