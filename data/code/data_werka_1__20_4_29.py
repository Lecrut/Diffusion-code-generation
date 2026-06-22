epsilon_compare = lambda a, b, epsilon=1e-9: abs(a - b) < epsilon

if __name__ == '__main__':
    print(epsilon_compare(0.1 + 0.2, 0.3))
    print(epsilon_compare(0.1, 0.2))