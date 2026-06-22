import math

MAX_EXPONENT_LIMIT = 1000

def power(base, exponent):
    if abs(exponent) > MAX_EXPONENT_LIMIT:
        raise ValueError("Exponent exceeds limit")
    return math.pow(base, exponent)

if __name__ == '__main__':
    SAMPLE_BASE = 5.0
    SAMPLE_EXPONENT = -2.0
    output = power(SAMPLE_BASE, SAMPLE_EXPONENT)
    print(output)