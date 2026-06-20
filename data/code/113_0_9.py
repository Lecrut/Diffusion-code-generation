class ArithmeticOperations:
    @staticmethod
    def subtract_amounts(a, b):
        return a - b

if __name__ == '__main__':
    result = ArithmeticOperations.subtract_amounts(10, 5)
    print(result)