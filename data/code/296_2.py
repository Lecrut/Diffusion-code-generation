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
    b = 4
    manager = RatioManager(a, b)
    print(f"Initial ratio of {a} and {b}: {manager.get_ratio()}")
    factor = 2
    manager.multiply_ratio(factor)
    print(f"Ratio multiplied by {factor}: {manager.get_ratio()}")
    divisor = 5
    manager.divide_ratio(divisor)
    print(f"Ratio divided by {divisor}: {manager.get_ratio()}")