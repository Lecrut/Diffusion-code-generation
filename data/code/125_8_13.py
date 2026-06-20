class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    print(f"Addition: {MathOperations.add(num1, num2)}")
    print(f"Subtraction: {MathOperations.subtract(10, 4)}")