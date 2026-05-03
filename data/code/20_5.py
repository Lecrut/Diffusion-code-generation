if __name__ == '__main__':
    a, b, epsilon = 1e-9, 2.00000000001, 1e-9
    result = lambda x, y, tol: abs(x - y) < tol
    print(result(a, b, epsilon))