class Fibonacci:
    _memo = {0: 0, 1: 1}

    @staticmethod
    def calculate(n):
        if n not in Fibonacci._memo:
            Fibonacci._memo[n] = Fibonacci.calculate(n - 1) + Fibonacci.calculate(n - 2)
        return Fibonacci._memo[n]

if __name__ == '__main__':
    nth_fibonacci = Fibonacci.calculate(10)
    print(nth_fibonacci)