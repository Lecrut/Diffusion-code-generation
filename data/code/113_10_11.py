class MathOperations:
    def calculate_difference(self, a, b):
        return a - b

if __name__ == '__main__':
    math_ops = MathOperations()
    result1 = math_ops.calculate_difference(10, 5)
    print(result1)
    result2 = math_ops.calculate_difference(20, 8)
    print(result2)