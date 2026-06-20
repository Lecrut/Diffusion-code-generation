class MathOperations:
    @staticmethod
    def calculate_difference(a, b):
        return a - b

if __name__ == '__main__':
    value1 = 25
    value2 = 9
    result = MathOperations.calculate_difference(value1, value2)
    print(result)