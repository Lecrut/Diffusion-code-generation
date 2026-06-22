class FactorialCalculator:
    def __init__(self):
        self._cache = {0: 1, 1: 1}

    def calculate(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n in self._cache:
            return self._cache[n]
        
        base_val = 1
        start_index = 0
        
        for cached_val, cached_idx in sorted(self._cache.items(), key=lambda x: x[0], reverse=True):
            if cached_idx > 0:
                base_val = cached_val
                start_index = cached_idx
                break
        
        result = base_val
        for i in range(start_index + 1, n + 1):
            result *= i
            self._cache[i] = result
        
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    print(calculator.calculate(0))
    print(calculator.calculate(1))
    print(calculator.calculate(5))
    print(calculator.calculate(12))
    print(calculator.calculate(20))
    try:
        print(calculator.calculate(-1))
    except ValueError:
        print("Caught expected error for negative input")
    try:
        print(calculator.calculate(3.5))
    except TypeError:
        print("Caught expected error for non-integer input")