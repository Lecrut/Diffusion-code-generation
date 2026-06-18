class NumberOperations:
    def calculate_difference(self, a, b):
        return a - b
if __name__ == '__main__':
    calculator = NumberOperations()
    num1 = 25
    num2 = 10
    result = calculator.calculate_difference(num1, num2)
    print(f"The difference between {num1} and {num2} is: {result}")