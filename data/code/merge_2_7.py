class MathOperations:
    @staticmethod
    def multiply(a, b):
        return a * b
if __name__ == '__main__':
    result = MathOperations.multiply(5, 10)
    print(result)
    result2 = MathOperations.multiply(12.5, 4)
    print(result2)