class ArithmeticOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def validate_operation(self, operation):
        if operation not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operation")
    
    def execute_operation(self, operation):
        self.validate_operation(operation)
        if operation == '+':
            return self.add()
        elif operation == '-':
            return self.subtract()
        elif operation == '*':
            return self.multiply()
        elif operation == '/':
            return self.divide()
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.num1 / self.num2

if __name__ == '__main__':
    calculator = ArithmeticOperations(10.5, 3.2)
    print(f"Addition: {calculator.execute_operation('+')}")
    print(f"Subtraction: {calculator.execute_operation('-')}")
    print(f"Multiplication: {calculator.execute_operation('*')}")