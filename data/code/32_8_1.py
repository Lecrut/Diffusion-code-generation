def binary_to_hex(binary_string):
    if not binary_string:
        return '0'
    binary_string = binary_string.lstrip('0')
    if not binary_string:
        return '0'
    return hex(int(binary_string, 2))[2:].upper()

if __name__ == '__main__':
    test_cases = ['1010', '11110000', '0000', '1', '0001010', '110011001100']
    for test in test_cases:
        print(binary_to_hex(test))