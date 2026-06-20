class FactorialCalculator:
    _memo = {0: 1, 1: 1}

    @staticmethod
    def factorial(n):
        if n not in FactorialCalculator._memo:
            FactorialCalculator._memo[n] = n * FactorialCalculator.factorial(n - 1)
        return FactorialCalculator._memo[n]
if __name__ == '__main__':
    result = FactorialCalculator.factorial(5)
    print(result)