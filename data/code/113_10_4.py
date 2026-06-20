class MathOperations:
    @staticmethod
    def calculate_difference(a, b):
        return a - b

if __name__ == '__main__':
    result = MathOperations.calculate_difference(10, 5)
    print(result)