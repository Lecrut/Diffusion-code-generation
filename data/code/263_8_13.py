class FibonacciCalculator:

    def __init__(self):
        self.memo = {0: 0, 1: 1}

    def nth_fibonacci(self, n):
        if n not in self.memo:
            self.memo[n] = self.nth_fibonacci(n - 1) + self.nth_fibonacci(n - 2)
        return self.memo[n]
if __name__ == '__main__':
    calc = FibonacciCalculator()
    print(calc.nth_fibonacci(5))
    print(calc.nth_fibonacci(10))