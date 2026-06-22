import math

def are_decimals_equal(a, b, epsilon=1e-09):
    if math.isnan(a) or math.isnan(b):
        return a == b
    if math.isinf(a) or math.isinf(b):
        return a == b
    return abs(a - b) <= epsilon
if __name__ == '__main__':
    print(are_decimals_equal(0.1 + 0.2, 0.3))
    print(are_decimals_equal(math.inf, math.inf))
    print(are_decimals_equal(float('nan'), float('nan')))
    print(are_decimals_equal(0.1 + 0.2, 0.3, epsilon=1e-10))