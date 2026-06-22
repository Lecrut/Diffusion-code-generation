class GreaterThanChecker:
    def __init__(self):
        self.samples = [
            (10, 5),
            (2, 4),
            (-1, -3)
        ]

    def is_greater(self, a, b):
        return a > b

    def check_samples(self):
        results = []
        for num1, num2 in self.samples:
            result = self.is_greater(num1, num2)
            results.append((num1, num2, result))
        return results

if __name__ == '__main__':
    checker = GreaterThanChecker()
    results = checker.check_samples()
    for num1, num2, result in results:
        print(f"{num1} is {'strictly greater' if result else 'not strictly greater'} than {num2}")