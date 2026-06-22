def is_negative(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -3.5, 2.7]
    for value in sample_values:
        print(f"{value}: {is_negative(value)}")