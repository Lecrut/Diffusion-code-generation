class NumberChecker:
    def __init__(self):
        self.test_values = [4, 5, 0, -2, -3]

    def is_even(self, n):
        return n & 1 == 0

    def check_values(self):
        results = {n: "even" if self.is_even(n) else "odd" for n in self.test_values}
        return results

if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_values())