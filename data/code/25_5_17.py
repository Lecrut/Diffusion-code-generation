import math

def is_zero(x):
    return abs(float(x)) < 1e-9 if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    test_values = [0, -0.0, 1e-8, -1e-8, 2**32456789 % 2]
    for val in test_values:
        result = is_zero(val)
        print(f"{val} -> {result}")