def is_positive(value):
    return value > 0.0

if __name__ == '__main__':
    sample_values = [1.5, -2.3, 0.0, 1e-10, -1e-10]
    results = {value: is_positive(value) for value in sample_values}
    print(results)