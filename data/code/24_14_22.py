def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [-1, 0, 1, -5.5, 3.2]
    for val in sample_values:
        print(is_negative(val))