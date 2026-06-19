def is_positive_float(value):
    return value > 0.0

if __name__ == '__main__':
    sample_values = [1.5, -2.3, 0.0, 4.7, -0.0]
    results = {value: is_positive_float(value) for value in sample_values}
    print(results)