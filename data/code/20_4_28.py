def are_equal(a, b, epsilon=1e-9):
    return abs(a - b) < epsilon

if __name__ == '__main__':
    print(are_equal(0.1 + 0.2, 0.3))