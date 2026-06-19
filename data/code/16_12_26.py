def is_positive(value):
    return value > 0

if __name__ == '__main__':
    sample_values = [1, -2, 3.5, 0, -0.1]
    results = [is_positive(val) for val in sample_values]
    print(results)