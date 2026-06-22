def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return "0x0"
    
    try:
        decimal_value = int(binary_string, 2)
    except ValueError:
        return "Error: Invalid binary input"
    
    return hex(decimal_value)

if __name__ == '__main__':
    binary_input = "11010110"
    result = binary_to_hex(binary_input)
    print(result)