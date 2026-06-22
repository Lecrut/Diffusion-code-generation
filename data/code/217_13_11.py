class NumberOperations:
    def __init__(self):
        self.a = 10
        self.b = 5

    @staticmethod
    def calculate_sum(x, y):
        return x + y

    @staticmethod
    def calculate_difference(x, y):
        return x - y

    @staticmethod
    def calculate_product(x, y):
        return x * y

    @staticmethod
    def calculate_integer_division(x, y):
        if y != 0:
            return x // y
        else:
            raise ValueError("Division by zero is not allowed")

if __name__ == '__main__':
    operations = NumberOperations()
    print(f"Sum: {NumberOperations.calculate_sum(operations.a, operations.b)}")
    print(f"Difference: {NumberOperations.calculate_difference(operations.a, operations.b)}")
    print(f"Product: {NumberOperations.calculate_product(operations.a, operations.b)}")
    try:
        print(f"Integer Division: {NumberOperations.calculate_integer_division(operations.a, operations.b)}")
    except ValueError as e:
        print(e)