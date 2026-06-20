class PrecisionMultiplier:
    MAX_PRECISION = 100

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return round(a * b, PrecisionMultiplier.MAX_PRECISION)

if __name__ == '__main__':
    result = PrecisionMultiplier.multiply(3.141592653589793, 2.718281828459045)
    print(result)