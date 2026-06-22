import math

def compute_power(base: float, exponent: float) -> float:
    return math.pow(base, exponent)

if __name__ == '__main__':
    result = compute_power(2.0, 10.0)
    print(result)