def get_parity(number):
    return (number, number % 2 == 0)

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, -1, -2, -3]
    results = [get_parity(value) for value in sample_values]
    print(results)