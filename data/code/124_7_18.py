class NumberOperations:
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
            return "Division by zero"

    def calculate_modulus(self):
        return self.x % self.y

if __name__ == '__main__':
    x = 12
    y = 3
    calculator = NumberOperations(x, y)
    print(f"Sum: {calculator.calculate_sum()}, Difference: {calculator.calculate_difference()}, Product: {calculator.calculate_product()}")
    print(f"Quotient: {calculator.calculate_quotient()}, Modulus: {calculator.calculate_modulus()}")