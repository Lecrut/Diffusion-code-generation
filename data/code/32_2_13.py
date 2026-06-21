import binascii

def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        raise ValueError("Input string cannot be empty")
    
    cleaned = binary_string.strip()
    if not cleaned:
        raise ValueError("Input string cannot be empty after stripping")
    
    if not all(c in '01' for c in cleaned):
        raise ValueError("Input must contain only binary digits 0 and 1")
    
    if len(cleaned) % 4 != 0:
        padding_length = 4 - (len(cleaned) % 4)
        cleaned = '0' * padding_length + cleaned
    
    decimal_value = int(cleaned, 2)
    return format(decimal_value, 'X')

if __name__ == '__main__':
    sample_binary_1 = "1101"
    sample_binary_2 = "10101010"
    sample_binary_3 = "000011111010"
    
    print(binary_to_hex(sample_binary_1))
    print(binary_to_hex(sample_binary_2))
    print(binary_to_hex(sample_binary_3))