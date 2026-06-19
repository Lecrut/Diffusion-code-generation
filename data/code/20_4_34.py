is_close = lambda a, b, epsilon=1e-9: abs(a - b) < epsilon

if __name__ == '__main__':
    print(is_close(0.1 + 0.2, 0.3))