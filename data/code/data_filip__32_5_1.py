import binascii

def binary_string_to_hex(binary_str: str) -> str:
    if not binary_str:
        return ""
    
    padding_needed = (8 - len(binary_str) % 8) % 8
    padded_binary = binary_str.zfill(len(binary_str) + padding_needed)
    
    hex_chars = []
    for i in range(0, len(padded_binary), 8):
        byte_chunk = padded_binary[i:i+8]
        dec_val = int(byte_chunk, 2)
        hex_chars.append(f"{dec_val:02x}")
    
    full_hex = "".join(hex_chars)
    
    if full_hex.startswith('0'):
        stripped = full_hex.lstrip('0')
        return stripped if stripped else '0'
    return full_hex

if __name__ == '__main__':
    sample_binary = "11110000101010101100110011111111"
    result = binary_string_to_hex(sample_binary)
    print(result)