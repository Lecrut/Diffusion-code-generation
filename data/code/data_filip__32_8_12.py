def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    if not all(c in '01' for c in binary_string):
        raise ValueError("Input must be a valid binary string")
    
    decimal_value = int(binary_string, 2)
    hex_string = hex(decimal_value)[2:]
    return hex_string.upper()

if __name__ == '__main__':
    test_cases = ["1111000010101010", "00000001", "1010", "0", "111111111111"]
    for case in test_cases:
        result = binary_to_hex(case)
        print(f"{case} -> {result}")