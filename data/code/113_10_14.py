class MathOperations:
    @staticmethod
    def calculate_difference(a, b):
        return a - b

if __name__ == '__main__':
    math_ops = MathOperations()
    result1 = math_ops.calculate_difference(20, 5)
    print(result1)
    result2 = math_ops.calculate_difference(30, 7)
    print(result2)