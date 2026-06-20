class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    num1 = 25
    num2 = 10
    print(MathOperations.add(num1, num2))
    print(MathOperations.subtract(num1, num2))