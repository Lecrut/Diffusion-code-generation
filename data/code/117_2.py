class NumberOperations:
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    calculator = NumberOperations()
    num1 = 25
    num2 = 10
    result = calculator.subtract(num1, num2)
    print(result)