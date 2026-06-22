is_zero = lambda x: abs(x) < 1e-15

if __name__ == '__main__':
    test_values = [0, -0.0, 123456789, 1e-16, 1e-14, 1]
    results = [is_zero(value) for value in test_values]
    print(results)