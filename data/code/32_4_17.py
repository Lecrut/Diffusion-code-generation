def binary_to_hex(binary_string):
    valid_chars = set('01')
    if not isinstance(binary_string, str):
        raise TypeError("Input must be a string")
    if len(binary_string) == 0:
        raise ValueError("Input string cannot be empty")
    
    for char in binary_string:
        if char not in valid_chars:
            raise ValueError(f"Invalid character '{char}' in binary string")
    
    decimal_value = int(binary_string, 2)
    hex_value = hex(decimal_value)
    return hex_value

if __name__ == '__main__':
    sample_binary = "101010"
    result = binary_to_hex(sample_binary)
    print(result)