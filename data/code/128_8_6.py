def check_negativity(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [-10, 5, -20, 3, -40]
    for val in sample_values:
        print(check_negativity(val))