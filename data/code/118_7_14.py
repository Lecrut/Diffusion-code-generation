class BitwiseMultiplier:
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31

    @staticmethod
    def multiply(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return a * b
        if a == 0 or b == 0:
            return 0
        negative_result = (a < 0) ^ (b < 0)
        a, b = (abs(a), abs(b))
        result = 0
        while b > 0:
            if b & 1:
                result += a
            a <<= 1
            b >>= 1
        return -result if negative_result else result
if __name__ == '__main__':
    print(BitwiseMultiplier.multiply(5, 3))
    print(BitwiseMultiplier.multiply(-5, 3))
    print(BitwiseMultiplier.multiply(-4, -2))