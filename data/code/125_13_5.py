class MathOperations:
    def calculate_sum_difference(self, a: int, b: int) -> (int, int):
        return (a + b, a - b)

if __name__ == '__main__':
    math_ops = MathOperations()
    result1 = math_ops.calculate_sum_difference(10, 4)
    result2 = math_ops.calculate_sum_difference(5, 3)
    print(result1)
    print(result2)