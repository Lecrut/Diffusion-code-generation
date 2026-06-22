class MathOperations:
    @staticmethod
    def add_values(a, b):
        return a + b

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result = MathOperations.add_values(num1, num2)
    print(result)

    num3 = -7
    num4 = 12
    result2 = MathOperations.add_values(num3, num4)
    print(result2)