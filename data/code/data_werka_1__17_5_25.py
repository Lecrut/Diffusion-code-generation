def get_number_and_parity(n):
    return (n, n % 2 == 0)

if __name__ == '__main__':
    sample_values = [42, -17, 0, 13, 256]
    for value in sample_values:
        result = get_number_and_parity(value)
        print(result)