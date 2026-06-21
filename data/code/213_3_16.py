class FibonacciCalculator:
    def __init__(self):
        self.memo = {0: 0, 1: 1}

    @staticmethod
    def calculate_nth_fibonacci(n, calculator=None):
        if calculator is None:
            calculator = FibonacciCalculator()
        if n in calculator.memo:
            return calculator.memo[n]
        else:
            calculator.memo[n] = calculator.calculate_nth_fibonacci(n - 1, calculator) + calculator.calculate_nth_fibonacci(n - 2, calculator)
            return calculator.memo[n]

if __name__ == '__main__':
    sample_value = 10
    fibonacci_value = FibonacciCalculator.calculate_nth_fibonacci(sample_value)
    print(f"Fibonacci number at position {sample_value}: {fibonacci_value}")