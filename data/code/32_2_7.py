def binary_to_hex(binary_string):
    if not binary_string:
        raise ValueError("Input cannot be empty")
    if any(c not in '01' for c in binary_string):
        raise ValueError("Input must contain only 0s and 1s")
    decimal_value = int(binary_string, 2)
    return format(decimal_value, 'X')

if __name__ == '__main__':
    test_cases = ['1010', '11110000', '0', '111111111111', '100000000']
    for binary in test_cases:
        print(binary_to_hex(binary))