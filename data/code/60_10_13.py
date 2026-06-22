class FactorialCalculator:
    def __init__(self):
        self.last_result = None

    def compute(self, n):
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
        product = 1
        multiplier = 2
        while multiplier <= n:
            product *= multiplier
            multiplier += 1
        self.last_result = product
        return product

    def get_last_computation(self):
        return self.last_result

def calculate_factorial(n):
    calculator = FactorialCalculator()
    return calculator.compute(n)

if __name__ == '__main__':
    calc_instance = FactorialCalculator()
    print(calculate_factorial(0))
    print(calculate_factorial(1))
    print(calc_instance.compute(5))
    print(calc_instance.compute(10))
    print(calc_instance.get_last_computation())