def get_parity(number):
    return (number, number % 2 == 0)

if __name__ == '__main__':
    sample_values = [42, 17, 0, -3, 256]
    results = [get_parity(value) for value in sample_values]
    print(results)