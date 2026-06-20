class ArithmeticOperations:
    @staticmethod
    def subtract_amounts(num1, num2):
        return num1 - num2

if __name__ == '__main__':
    result = ArithmeticOperations.subtract_amounts(15, 7)
    print(result)