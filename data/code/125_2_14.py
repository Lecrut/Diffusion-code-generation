class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    print(MathOperations.add(5, 3))
    print(MathOperations.subtract(10, 4))