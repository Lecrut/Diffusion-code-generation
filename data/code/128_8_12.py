def check_negativity(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [10, -5, 20, -1, 33, -12, 0]
    for number in sample_values:
        print(check_negativity(number))