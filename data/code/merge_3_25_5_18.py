def is_zero(x): return x == 0 if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    test_values = [0, -1e-38, 1e-39, 2.5, int(0), None]
    for val in test_values:
        print(f"{val!r}: {is_zero(val)}")