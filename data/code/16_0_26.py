def is_positive(number):
    return number > 0

if __name__ == '__main__':
    sample_values = [1, -1, 0, 2.5, -3.6]
    for value in sample_values:
        print(is_positive(value))