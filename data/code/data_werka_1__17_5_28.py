def get_parity(number):
    return (number, number % 2 == 0)

if __name__ == '__main__':
    sample_values = [42, 7, 0, -3, 15]
    for value in sample_values:
        print(get_parity(value))