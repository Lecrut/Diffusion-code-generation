def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        raise ValueError("Input string cannot be empty")
    if any(char not in '01' for char in binary_string):
        raise ValueError("Input must contain only 0s and 1s")
    decimal_value = int(binary_string, 2)
    hex_string = format(decimal_value, 'X')
    return hex_string

if __name__ == '__main__':
    test_cases = ['1010', '1111', '10000', '0', '11001100']
    for case in test_cases:
        result = binary_to_hex(case)
        print(f"{case} -> {result}")