def is_positive(x):
    return x > 0

if __name__ == '__main__':
    sample_values = [1, -2, 3.5, 0]
    for value in sample_values:
        print(is_positive(value))