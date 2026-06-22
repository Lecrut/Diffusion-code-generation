TOLERANCE = 1e-9

are_close = lambda x, y, epsilon=TOLERANCE: abs(x - y) < epsilon

if __name__ == '__main__':
    result = are_close(0.1 + 0.2, 0.3)
    print(result)