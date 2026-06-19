EPSILON = 1e-9

is_equal = lambda x, y: abs(x - y) < EPSILON

if __name__ == '__main__':
    print(is_equal(0.1 + 0.2, 0.3))