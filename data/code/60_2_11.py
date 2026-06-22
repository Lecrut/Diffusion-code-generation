class FactorialCalculator:
    def compute(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == '__main__':
    calculator = FactorialCalculator()
    values_to_test = [0, 1, 5, 10]
    for value in values_to_test:
        print(f"{value}! = {calculator.compute(value)}")