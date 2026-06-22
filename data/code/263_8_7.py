class FibonacciCalculator:

    def __init__(self):
        self.memo = {0: 0, 1: 1}

    def fibonacci(self, n):
        if n not in self.memo:
            self.memo[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        return self.memo[n]
if __name__ == '__main__':
    calc = FibonacciCalculator()
    print(calc.fibonacci(5))
    print(calc.fibonacci(10))