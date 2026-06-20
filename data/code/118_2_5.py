import operator

class MathOperations:
    @staticmethod
    def multiply(a, b):
        return operator.mul(a, b)

if __name__ == '__main__':
    result = MathOperations.multiply(9, 8)
    print(result)