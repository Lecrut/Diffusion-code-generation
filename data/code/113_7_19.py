class ArithmeticOperations:
    MINUS_ONE = 1

    @staticmethod
    def subtract(a):
        return a - ArithmeticOperations.MINUS_ONE

if __name__ == '__main__':
    result = ArithmeticOperations.subtract(10)
    print(result)