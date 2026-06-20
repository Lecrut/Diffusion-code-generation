def compare_floats(a, b):
    return a > b

if __name__ == '__main__':
    print(compare_floats(0.1 + 0.2, 0.3))
    print(compare_floats(1.0, 1.0))
    print(compare_floats(1e-9, -1e-9))