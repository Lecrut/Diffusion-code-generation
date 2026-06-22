import math

def compute_power(base, exponent):
    return math.pow(base, exponent)

if __name__ == '__main__':
    result = compute_power(2, 3)
    print(result)
    result2 = compute_power(5, 0.5)
    print(result2)
    result3 = compute_power(10, -1)
    print(result3)