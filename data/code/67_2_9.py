class ArithmeticOperations:
    ADDITION_CONSTANT = 1

    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    result = ArithmeticOperations.add(7.5, 2.5)
    print(result)