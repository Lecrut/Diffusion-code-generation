class ArithmeticOperations:
    def multiply(self, num1, num2):
        return num1 * num2

if __name__ == '__main__':
    arithmetic = ArithmeticOperations()
    result1 = arithmetic.multiply(4, 3)
    result2 = arithmetic.multiply(5, 6)
    print(result1)
    print(result2)