EPSILON = 1e-09
are_equal = lambda x, y: abs(x - y) < EPSILON
if __name__ == '__main__':
    print(are_equal(0.1 + 0.2, 0.3))
    print(are_equal(0.1, 0.2))