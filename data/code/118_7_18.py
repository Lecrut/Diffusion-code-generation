class MathOperations:
    @staticmethod
    def multiply(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a * b
        else:
            return a * b

if __name__ == '__main__':
    result = MathOperations.multiply(5, 3)
    print(result)