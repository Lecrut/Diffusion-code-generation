class MathOperations:
    @staticmethod
    def add(num1, num2):
        return num1 + num2
    
    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

if __name__ == '__main__':
    print(MathOperations.add(15, 27))
    print(MathOperations.subtract(10, 4))