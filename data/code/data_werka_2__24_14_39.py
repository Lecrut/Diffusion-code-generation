def is_negative(value):
    if value < 0:
        return True
    return False

if __name__ == '__main__':
    sample_values = [-10, 5, 0, -2.718, 3.14]
    for val in sample_values:
        print(is_negative(val))