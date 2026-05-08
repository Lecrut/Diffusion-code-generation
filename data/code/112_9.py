class Sum:
    def __init__(self, a, b):
        self.result = a + b
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    calculator = Sum(num1, num2)
    print(calculator.result)