class MathOperations:
    @classmethod
    def multiply(cls, a, b):
        result = 0
        for _ in range(abs(b)):
            if b > 0:
                result += a
            else:
                result -= a
            a <<= 1
        return result if b >= 0 else -result

if __name__ == '__main__':
    sample_a = 5
    sample_b = 3
    print(MathOperations.multiply(sample_a, sample_b))