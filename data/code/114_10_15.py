class MathOperations:
    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = MathOperations.multiply(num1, num2)
    print(result)