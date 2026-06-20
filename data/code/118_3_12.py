class LargeNumberCalculator:
    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    num1 = 3456789012345678901234567890
    num2 = 9876543210987654321098765432
    product = LargeNumberCalculator.multiply(num1, num2)
    print(product)