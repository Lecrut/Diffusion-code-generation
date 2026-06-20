class ArithmeticOperations:
    def __init__(self):
        self.NUM1 = 15
        self.NUM2 = 7

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    arithmetic = ArithmeticOperations()
    sum_result = ArithmeticOperations.add(arithmetic.NUM1, arithmetic.NUM2)
    difference_result = ArithmeticOperations.subtract(arithmetic.NUM1, arithmetic.NUM2)
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")