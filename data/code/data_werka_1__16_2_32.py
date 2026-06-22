def is_positive(x):
    return x > 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, 3.14, -2.71]
    for value in sample_values:
        print(is_positive(value))