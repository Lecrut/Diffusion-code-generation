def are_near_equal(a, b, tolerance=1e-9):
    return abs(a - b) <= tolerance

if __name__ == '__main__':
    print(are_near_equal(0.1 + 0.2, 0.3))
    print(are_near_equal(1.0, 1.000000001))