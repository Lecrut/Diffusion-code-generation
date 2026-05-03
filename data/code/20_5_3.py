if __name__ == '__main__':
    a, b, epsilon = 1e-9, 2.718281828459045, 1e-12
    result = lambda x, y, tol: abs(x - y) < tol
    print(result(a, b, epsilon))