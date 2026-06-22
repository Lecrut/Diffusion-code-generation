def decimal_to_binary(n):
    if n == 0:
        return '0'
    if n < 0:
        return '-' + decimal_to_binary(-n)
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n >> 1
    return binary

if __name__ == '__main__':
    test_values = [0, 1, 2, 5, 10, 255, 1023]
    for value in test_values:
        print(decimal_to_binary(value))