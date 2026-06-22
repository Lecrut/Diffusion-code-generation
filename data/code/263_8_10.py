class Fibonacci:

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            result = n
        else:
            result = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = result
        return result
if __name__ == '__main__':
    fib_instance = Fibonacci()
    print(fib_instance.fib(5))
    print(fib_instance.fib(10))