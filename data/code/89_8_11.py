class OperationEvaluator:

    def evaluate(self, num1, num2, operation):
        if operation == '+':
            return self.add(num1, num2)
        elif operation == '-':
            return self.subtract(num1, num2)
        elif operation == '*':
            return self.multiply(num1, num2)
        elif operation == '/':
            return self.divide(num1, num2)
        else:
            raise ValueError('Unsupported operation')

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError('Division by zero')
        return a / b
if __name__ == '__main__':
    evaluator = OperationEvaluator()
    result = evaluator.evaluate(10, 5, '+')
    print(result)