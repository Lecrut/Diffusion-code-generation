def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [-10, 5, 0, -2.718, 3.1415]
    for val in sample_values:
        print(is_negative(val))