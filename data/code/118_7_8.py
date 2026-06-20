class MathOperations:

    def multiply(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return self._multiply_bitwise(a, b)
        else:
            return a * b

    def _multiply_bitwise(self, a, b):
        result = 0
        for i in range(abs(b)):
            result += a
        if b < 0:
            result = -result
        return result
if __name__ == '__main__':
    math_ops = MathOperations()
    print(math_ops.multiply(5, 3))
    print(math_ops.multiply(-5, 3))
    print(math_ops.multiply(-4, -2))
    print(math_ops.multiply(0, 5))
    print(math_ops.multiply(-10, 0))
    print(math_ops.multiply(5, -3))