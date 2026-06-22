def are_decimals_equal(a, b, epsilon=1e-09):
    if a != a or b != b:
        return False
    if a == float('inf') or a == float('-inf') or b == float('inf') or (b == float('-inf')):
        return a == b
    return abs(a - b) < epsilon
if __name__ == '__main__':
    print(are_decimals_equal(0.1 + 0.2, 0.3))
    print(are_decimals_equal(float('nan'), float('nan')))
    print(are_decimals_equal(float('inf'), float('inf')))
    print(are_decimals_equal(float('-inf'), float('-inf')))
    print(are_decimals_equal(float('inf'), float('-inf')))