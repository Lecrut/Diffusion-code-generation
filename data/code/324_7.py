class Calculator:
    def __init__(self, a, b):
        self.attribute_a = a
        self.attribute_b = b
    def calculate_product(self):
        return self.attribute_a * self.attribute_b
if __name__ == '__main__':
    calc = Calculator(5, 10)
    result = calc.calculate_product()
    print(result)