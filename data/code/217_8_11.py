import math

def compare_decimals(a, b, epsilon=1e-09):
    if math.isnan(a) or math.isnan(b):
        return False
    if math.isinf(a) or math.isinf(b):
        return a == b
    return abs(a - b) < epsilon
if __name__ == '__main__':
    print(compare_decimals(0.1 + 0.2, 0.3))
    print(compare_decimals(float('nan'), float('nan')))
    print(compare_decimals(float('inf'), float('inf')))
    print(compare_decimals(float('-inf'), float('-inf')))
    print(compare_decimals(float('inf'), float('-inf')))