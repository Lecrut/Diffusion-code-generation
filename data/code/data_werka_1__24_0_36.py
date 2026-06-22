def is_negative(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -3.5, 200]
    for value in sample_values:
        print(is_negative(value))