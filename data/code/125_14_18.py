class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    addition_result = MathOperations.add(num1, num2)
    subtraction_result = MathOperations.subtract(num1, num2)
    
    assert addition_result == 15, "Addition test failed"
    assert subtraction_result == 5, "Subtraction test failed"
    
    print(f"Addition of {num1} and {num2} is: {addition_result}")
    print(f"Subtraction of {num1} and {num2} is: {subtraction_result}")