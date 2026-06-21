def validate_and_convert_binary_to_hex(binary_input: str) -> str:
    if not binary_input:
        raise ValueError("Input cannot be empty")
    
    for char in binary_input:
        if char not in '01':
            raise ValueError(f"Invalid character '{char}' found in binary input")
    
    decimal_value = int(binary_input, 2)
    hex_value = hex(decimal_value)
    
    return hex_value.upper()[2:]

if __name__ == '__main__':
    result = validate_and_convert_binary_to_hex('1101010')
    print(result)