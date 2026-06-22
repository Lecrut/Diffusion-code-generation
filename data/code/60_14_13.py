class FactorialCalculator:
    def __init__(self):
        self._cache = {0: 1}

    def calculate(self, n):
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n in self._cache:
            return self._cache[n]
        result = self._cache[n - 1]
        current = n
        while current > 0:
            if current not in self._cache:
                self._cache[current] = self._cache[current - 1] * current
            else:
                break
            current -= 1
        if n > 0:
            val = self._cache[n - 1] * n
            self._cache[n] = val
            return val
        return 1

    def reset_cache(self):
        self._cache = {0: 1}

if __name__ == '__main__':
    calc = FactorialCalculator()
    print(calc.calculate(5))
    print(calc.calculate(0))
    print(calc.calculate(10))
    print(calc.calculate(7))
    calc.reset_cache()
    print(calc.calculate(3))