def are_close(a, b, tolerance=1e-9):
    return abs(a - b) <= tolerance

if __name__ == '__main__':
    print(are_close(0.1 + 0.2, 0.3))