def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [-5, 0, 3]
    for val in sample_values:
        print(is_negative(val))