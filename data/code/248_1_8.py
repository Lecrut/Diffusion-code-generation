class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = MathOperations.add_numbers(num1, num2)
    print(result)