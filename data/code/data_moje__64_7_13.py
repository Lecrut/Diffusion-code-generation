import math

def power(base, exponent):
    result = base ** exponent
    return float(result)

if __name__ == '__main__':
    print(power(2, 3))
    print(power(9, 0.5))
    print(power(2.5, 2))