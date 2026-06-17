class RatioManager:
    def __init__(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot calculate ratio when the second number is zero")
        self.ratio = num1 / num2
    def multiply_ratio(self, factor):
        self.ratio *= factor
    def divide_ratio(self, divisor):
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide ratio by zero")
        self.ratio /= divisor
    def get_ratio(self):
        return self.ratio
if __name__ == '__main__':
    a = 10
    b = 5
    rm = RatioManager(a, b)
    print(f"Initial ratio of {a} and {b}: {rm.get_ratio()}")
    factor = 2
    rm.multiply_ratio(factor)
    print(f"Ratio multiplied by {factor}: {rm.get_ratio()}")
    divisor = 4
    rm.divide_ratio(divisor)
    print(f"Ratio divided by {divisor}: {rm.get_ratio()}")