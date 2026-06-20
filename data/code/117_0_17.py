class MathOperations:
    def calculate_difference(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    calculator = MathOperations()
    difference1 = calculator.calculate_difference(15, 7)
    difference2 = calculator.calculate_difference(3.5, 2.1)
    print(difference1)
    print(difference2)