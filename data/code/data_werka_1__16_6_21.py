def is_positive(value):
    return value > 0.0

if __name__ == '__main__':
    sample_values = [3.14, -2.71, 0.0, 1e-10, -1e-10]
    for val in sample_values:
        print(f"{val} is positive: {is_positive(val)}")