class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_sum(self):
        return self.x + self.y

    def calculate_difference(self):
        return self.x - self.y

    def calculate_product(self):
        return self.x * self.y

    def calculate_quotient(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return None

    def calculate_modulus(self):
        return self.x % self.y

if __name__ == '__main__':
    calc = Calculator(12, 3)
    print(f"Sum: {calc.calculate_sum()}, Difference: {calc.calculate_difference()}, Product: {calc.calculate_product()}")
    print(f"Quotient: {calc.calculate_quotient()}, Modulus: {calc.calculate_modulus()}")