def is_positive_float(value):
    return value > 0.0

if __name__ == '__main__':
    sample_values = [3.14, -2.71, 0.0, 1e-10, -1e-10]
    results = {value: is_positive_float(value) for value in sample_values}
    print(results)