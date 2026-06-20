class MathOperations:

    @staticmethod
    def _multiply_bitwise(a, b):
        result = 0
        while b > 0:
            if b & 1:
                result += a
            a <<= 1
            b >>= 1
        return result

    @classmethod
    def multiply(cls, a, b):
        return cls._multiply_bitwise(a, abs(b)) * (1 if b >= 0 else -1)
if __name__ == '__main__':
    result = MathOperations.multiply(5, 3)
    print(result)
    result = MathOperations.multiply(-4, 6)
    print(result)
    result = MathOperations.multiply(7, -8)
    print(result)