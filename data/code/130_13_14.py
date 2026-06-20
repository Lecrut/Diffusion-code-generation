def is_zero(number):
    return number == 0

if __name__ == '__main__':
    sample_values = [1, 0, 3, 4, 5, 10, 20, 0, 7, 8, 0]
    for value in sample_values:
        print(is_zero(value))