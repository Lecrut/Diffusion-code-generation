def is_positive(value):
    return value > 0.0

if __name__ == '__main__':
    sample_values = [3.14, -2.71, 0.0, 1e-10, -1e-10]
    for value in sample_values:
        print(is_positive(value))