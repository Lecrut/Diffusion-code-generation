def are_floats_near(a, b, tolerance=1e-9):
    return abs(a - b) <= tolerance

if __name__ == '__main__':
    print(are_floats_near(0.1 + 0.2, 0.3))
    print(are_floats_near(1.0, 1.000000001))