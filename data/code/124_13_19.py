class ArithmeticOperations:
    def __init__(self):
        self.a = 10.5
        self.b = 2.5

    @staticmethod
    def calculate_sum(a, b):
        return a + b

    @staticmethod
    def calculate_difference(a, b):
        return a - b

    @staticmethod
    def calculate_product(a, b):
        return a * b

    @staticmethod
    def calculate_quotient(a, b):
        return a / b

if __name__ == '__main__':
    ops = ArithmeticOperations()
    print(ops.calculate_sum(ops.a, ops.b))
    print(ops.calculate_difference(ops.a, ops.b))
    print(ops.calculate_product(ops.a, ops.b))
    print(ops.calculate_quotient(ops.a, ops.b))