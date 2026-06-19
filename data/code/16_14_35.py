def is_positive(number):
    return number > 0

if __name__ == '__main__':
    sample_values = [0, -1, 2.5, -3.7, 10]
    for value in sample_values:
        print(f"{value}: {is_positive(value)}")