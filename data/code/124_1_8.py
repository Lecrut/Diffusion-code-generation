class ArithmeticOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def floor_divide(x, y):
        return x // y

def basic_arithmetic(a, b):
    return {
        'addition': ArithmeticOperations.add(a, b),
        'subtraction': ArithmeticOperations.subtract(a, b),
        'multiplication': ArithmeticOperations.multiply(a, b),
        'floor_division': ArithmeticOperations.floor_divide(a, b)
    }

if __name__ == '__main__':
    result = basic_arithmetic(10, 4)
    print(result)