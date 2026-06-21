def get_parity(number):
    return (number, number % 2 == 0)

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2, -2, 3, -3, 4, -4]
    for value in sample_values:
        print(get_parity(value))