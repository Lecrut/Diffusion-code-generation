def binary_to_hex(binary_str):
    if not binary_str:
        return "0"
    
    padding_length = (8 - len(binary_str) % 8) % 8
    padded_binary = '0' * padding_length + binary_str
    
    bytes_list = [padded_binary[i:i+8] for i in range(0, len(padded_binary), 8)]
    
    byte_values = [int(byte, 2) for byte in bytes_list]
    
    hex_chars = [hex(val)[2:].upper() for val in byte_values]
    
    if len(hex_chars) > 1:
        hex_chars[0] = hex_chars[0].lstrip('0') or '0'
        
    result = ''.join(hex_chars)
    return result if result else "0"

if __name__ == '__main__':
    sample_binary = "110110111011"
    hex_result = binary_to_hex(sample_binary)
    print(hex_result)