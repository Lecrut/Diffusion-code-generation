def binary_to_hex(binary_string):
    if not binary_string:
        return '0'
    
    cleaned = binary_string.lstrip('0')
    if not cleaned:
        return '0'
    
    decimal_value = int(cleaned, 2)
    hex_string = hex(decimal_value)[2:]
    
    if not hex_string:
        return '0'
    
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    
    return hex_string.upper()

if __name__ == '__main__':
    samples = [
        "0000",
        "00010101",
        "11111111",
        "101010101010",
        "",
        "0",
        "00000001"
    ]
    for s in samples:
        print(binary_to_hex(s))