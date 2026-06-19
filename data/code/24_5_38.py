def is_strictly_less_than_zero(num):
    return num < 0

if __name__ == '__main__':
    sample_values = [-1.5, -0.0, 0.0, 1.234, -1e-10, 1e-10]
    results = [is_strictly_less_than_zero(value) for value in sample_values]
    print(results)