class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b

if __name__ == '__main__':
    result_add = MathOperations.add(5, 3)
    result_subtract = MathOperations.subtract(10, 4)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")