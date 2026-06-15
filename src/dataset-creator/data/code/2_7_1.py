class MathOperations:
    @staticmethod
    def multiply(a, b):
        return a * b
if __name__ == '__main__':
    result = MathOperations.multiply(5, 10)
    print(result)
    result2 = MathOperations.multiply(3.5, 2)
    print(result2)