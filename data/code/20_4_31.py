epsilon_equal = lambda a, b, epsilon=1e-9: abs(a - b) < epsilon

if __name__ == '__main__':
    print(epsilon_equal(0.1 + 0.2, 0.3))