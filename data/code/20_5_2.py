if __name__ == '__main__':
    a, b, epsilon = 1e-9, 2.718281828459045, 1e-12
    compare = lambda x, y, eps: abs(x - y) < eps
    print(compare(a, b, epsilon))