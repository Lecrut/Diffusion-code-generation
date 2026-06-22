class NumberChecker:
    def __init__(self, value):
        self.value = value

    def check_positive(self):
        return self.value > 0

    def check_even(self):
        return self.value % 2 == 0

    def check_divisible_by_three(self):
        return self.value % 3 == 0

    def get_results(self):
        positive = self.check_positive()
        even = self.check_even()
        divisible_by_three = self.check_divisible_by_three()
        return {
            "value": self.value,
            "positive": positive,
            "even": even,
            "divisible_by_three": divisible_by_three
        }

if __name__ == '__main__':
    samples = [42, 7, -12, 0, 3]
    for s in samples:
        checker = NumberChecker(s)
        results = checker.get_results()
        print(results)