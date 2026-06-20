class MathOperations:
    @classmethod
    def multiply(cls, a, b):
        return a * b

if __name__ == '__main__':
    result = MathOperations.multiply(4, 3)
    print(result)