import math

def compute_power(base, exponent):
    result = math.pow(base, exponent)
    return result

if __name__ == '__main__':
    base = 2
    exponent = 10
    output = compute_power(base, exponent)
    print(output)