class ArithmeticOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    number1 = 42
    number2 = 53
    sum_result = ArithmeticOperations.add_numbers(number1, number2)
    print(sum_result)