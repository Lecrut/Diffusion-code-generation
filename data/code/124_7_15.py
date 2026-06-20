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
            return None

    def calculate_modulus(self):
        return self.x % self.y

if __name__ == '__main__':
    num_ops = NumberOperations(12, 3)
    print(f"Sum: {num_ops.calculate_sum()}, Difference: {num_ops.calculate_difference()}")
    print(f"Product: {num_ops.calculate_product()}, Quotient: {num_ops.calculate_quotient()}")
    print(f"Modulus: {num_ops.calculate_modulus()}")