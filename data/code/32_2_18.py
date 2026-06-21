def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    value = int(binary_string, 2)
    hex_string = format(value, 'x')
    return hex_string

if __name__ == '__main__':
    test_cases = ["1010", "11111111", "0", "10000000000", "110011001100"]
    for case in test_cases:
        print(binary_to_hex(case))