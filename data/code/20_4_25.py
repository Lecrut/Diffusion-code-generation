eps_equal = lambda x, y, epsilon=1e-9: abs(x - y) < epsilon

if __name__ == '__main__':
    print(eps_equal(0.1 + 0.2, 0.3))