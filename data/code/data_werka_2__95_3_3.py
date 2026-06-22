def check_value(value):
    return value > 0 and value % 2 == 0 and value < 100

if __name__ == '__main__':
    sample_values = [0, 2, 98, 100, -5]
    for val in sample_values:
        print(check_value(val))