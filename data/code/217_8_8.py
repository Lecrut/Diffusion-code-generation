import math

def is_nan(value):
    return value != value

def is_inf(value):
    return value == float('inf') or value == -float('inf')

def are_decimals_equal(a, b, epsilon=1e-09):
    if is_nan(a) or is_nan(b):
        return a == b
    if is_inf(a) or is_inf(b):
        return a == b
    return abs(a - b) <= epsilon

if __name__ == '__main__':
    print(are_decimals_equal(0.1 + 0.2, 0.3))
    print(are_decimals_equal(float('nan'), float('nan')))
    print(are_decimals_equal(float('inf'), float('inf')))
    print(are_decimals_equal(float('-inf'), float('-inf')))
    print(are_decimals_equal(float('inf'), float('-inf')))