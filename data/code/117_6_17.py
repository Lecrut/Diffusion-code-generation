class ArithmeticOperations:
    @staticmethod
    def calculate_difference(x, y):
        return x - y

if __name__ == '__main__':
    num1 = 34
    num2 = 17
    result = ArithmeticOperations.calculate_difference(num1, num2)
    print(result)