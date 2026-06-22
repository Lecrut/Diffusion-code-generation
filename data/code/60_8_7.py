FACTORIAL_BASE = 1
MIN_INPUT = 0

class FactorialCalculator:
    def __init__(self):
        self.cache = {}

    def compute(self, number):
        if number < MIN_INPUT:
            raise ValueError("Factorial is not defined for negative numbers")
        if number == 0 or number == 1:
            return FACTORIAL_BASE
        if number in self.cache:
            return self.cache[number]
        
        result = 1
        current = 2
        while current <= number:
            result *= current
            current += 1
        
        self.cache[number] = result
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    print(calculator.compute(5))
    print(calculator.compute(0))
    print(calculator.compute(10))