def hex_to_decimal(hex_str: str) -> int:
    if not isinstance(hex_str, str):
        raise TypeError("Input must be a string")
    
    try:
        decimal_value = int(hex_str, 16)
        return decimal_value
    except ValueError:
        raise ValueError("Input contains invalid hexadecimal characters")

if __name__ == '__main__':
    hex_string = "1A3F"
    result = hex_to_decimal(hex_string)
    print(result)