def is_negative(num):
    return num < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -3.5, 2]
    for value in sample_values:
        print(is_negative(value))