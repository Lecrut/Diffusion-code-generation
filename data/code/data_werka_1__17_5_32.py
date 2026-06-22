def get_number_and_parity(n):
    return n, n % 2 == 0

if __name__ == '__main__':
    sample_values = [42, 7, 0, -3, 15]
    results = [get_number_and_parity(value) for value in sample_values]
    print(results)