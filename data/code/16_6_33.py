def is_positive_float(value):
    return value > 0.0

if __name__ == '__main__':
    sample_values = [1.0, -1.0, 0.0, 1e-300, -1e-300]
    results = {value: is_positive_float(value) for value in sample_values}
    print(results)