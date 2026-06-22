class ArithmeticOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate_sum(self):
        return self.num1 + self.num2

    def calculate_difference(self):
        return self.num1 - self.num2

    def calculate_product(self):
        return self.num1 * self.num2

    def calculate_quotient(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Undefined"

if __name__ == '__main__':
    operation = ArithmeticOperations(20, 5)
    print("--- Arithmetic Operations ---")
    print(f"First Number: {operation.num1}")
    print(f"Second Number: {operation.num2}")
    print("-" * 30)
    print(f"Sum: {operation.calculate_sum()}")
    print(f"Difference: {operation.calculate_difference()}")
    print(f"Product: {operation.calculate_product()}")
    print(f"Quotient: {operation.calculate_quotient()}")