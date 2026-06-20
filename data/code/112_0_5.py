class ArithmeticOperations:
    NUM1 = 15
    NUM2 = 27

    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    result = ArithmeticOperations.add_numbers(ArithmeticOperations.NUM1, ArithmeticOperations.NUM2)
    print(result)