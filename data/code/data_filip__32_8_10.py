def binary_string_to_hex(binary_str):
    if not binary_str:
        return "0"
    binary_str = binary_str.lstrip('0')
    if not binary_str:
        return "0"
    num_value = int(binary_str, 2)
    return format(num_value, 'X')

if __name__ == '__main__':
    test_cases = ["1010", "00001111", "0000", "1", "0", "1111000011110000"]
    for test in test_cases:
        print(binary_string_to_hex(test))