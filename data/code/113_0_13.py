class ArithmeticOperations:
    @staticmethod
    def subtract_amounts(a, b):
        return a - b

if __name__ == '__main__':
    sample_values = {
        'num1': 15,
        'num2': 7
    }
    result = ArithmeticOperations.subtract_amounts(sample_values['num1'], sample_values['num2'])
    print(result)