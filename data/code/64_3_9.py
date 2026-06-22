import math

def compute_power(base, exponent):
    return math.pow(base, exponent)

if __name__ == '__main__':
    base = 2.0
    exponent = 3.5
    result = compute_power(base, exponent)
    print(result)