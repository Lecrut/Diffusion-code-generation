epsilon = 1e-9

are_equal = lambda x, y: abs(x - y) < epsilon

if __name__ == '__main__':
    print(are_equal(0.1 + 0.2, 0.3))