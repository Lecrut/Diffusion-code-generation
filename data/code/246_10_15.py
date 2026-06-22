class ArithmeticOperations:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    number1 = 15
    number2 = 27
    result = ArithmeticOperations.add(number1, number2)
    print(result)