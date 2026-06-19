epsilon_compare = lambda x, y, epsilon=1e-9: abs(x - y) < epsilon

if __name__ == '__main__':
    result = epsilon_compare(0.1 + 0.2, 0.3)
    print(result)