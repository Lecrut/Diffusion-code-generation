def is_zero(x): return x == 0 if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    test_values = [0, -0.0, 1e-25, 3.4, None]
    for val in test_values:
        print(f"{val!r} -> {is_zero(val)}")