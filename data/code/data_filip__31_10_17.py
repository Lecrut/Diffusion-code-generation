def hex_to_decimal(hex_string: str) -> int:
    hex_string = hex_string.strip()
    if not hex_string:
        return 0
    is_negative = False
    start_index = 0
    if hex_string.startswith('-'):
        is_negative = True
        start_index = 1
    elif hex_string.startswith('+'):
        start_index = 1
    
    if start_index >= len(hex_string):
        return 0
    
    hex_part = hex_string[start_index:]
    if not hex_part:
        return 0
        
    result = int(hex_part, 16)
    
    if is_negative:
        return -result
    return result

if __name__ == '__main__':
    sample_hex = "1a3f"
    decimal_value = hex_to_decimal(sample_hex)
    print(decimal_value)
    
    sample_hex_negative = "-ff"
    decimal_value_negative = hex_to_decimal(sample_hex_negative)
    print(decimal_value_negative)