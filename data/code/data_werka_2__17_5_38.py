def check_parity(number):
    return (number, number % 2 == 0)

if __name__ == '__main__':
    sample_values = [0, 1, 2, -3, -4, 7]
    for value in sample_values:
        print(check_parity(value))