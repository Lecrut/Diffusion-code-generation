class MathOperations:
    def subtract(self, a: int, b: int) -> int:
        return a - b

if __name__ == '__main__':
    math_ops = MathOperations()
    result = math_ops.subtract(10, 5)
    print(result)