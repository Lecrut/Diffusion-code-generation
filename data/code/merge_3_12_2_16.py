class RatioConverter:
    def __init__(self):
        pass

    @staticmethod
    def gcd(a, b):
        """Compute the Greatest Common Divisor of a and b using Euclidean algorithm."""
        while b != 0:
            a, b = b, a % b
        return abs(a)

if __name__ == '__main__':
    pass
