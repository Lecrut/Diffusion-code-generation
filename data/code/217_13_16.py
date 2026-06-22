class NumberOperations:
    def __init__(self, a=10, b=5):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def product(self):
        return self.a * self.b

    def integer_division(self):
        if self.b != 0:
            return self.a // self.b
        else:
            raise ValueError("Cannot divide by zero")

if __name__ == '__main__':
    operations = NumberOperations()
    print(f"Sum: {operations.sum()}")
    print(f"Difference: {operations.difference()}")
    print(f"Product: {operations.product()}")
    try:
        print(f"Integer Division: {operations.integer_division()}")
    except ValueError as e:
        print(e)