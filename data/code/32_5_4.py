import binascii

def binary_to_hex_chunked(binary_string: str, chunk_size: int = 4096) -> str:
    if not binary_string:
        return ''
    
    hex_chars = "0123456789abcdef"
    bit_to_val = {c: i for i, c in enumerate(binary_chars) for binary_chars in [hex_chars]}
    
    hex_chars_map = "0123456789abcdef"
    mapping = {0: 0, 1: 1}
    
    result_parts = []
    length = len(binary_string)
    
    for i in range(0, length, chunk_size):
        chunk = binary_string[i:i+chunk_size]
        padded_len = len(chunk)
        padding_needed = (4 - (padded_len % 4)) % 4
        if padding_needed:
            chunk = '0' * padding_needed + chunk
        
        hex_part = ''
        for j in range(0, len(chunk), 4):
            nibble = chunk[j:j+4]
            val = 0
            for bit in nibble:
                val = (val << 1) | int(bit)
            hex_part += hex_chars_map[val]
        
        result_parts.append(hex_part)
    
    return ''.join(result_parts)

def convert_large_binary_string(binary_string: str) -> str:
    if not binary_string:
        return ""
    
    chunk_size = 4096
    hex_chars = "0123456789abcdef"
    result = []
    
    total_len = len(binary_string)
    offset = 0
    
    while offset < total_len:
        end = min(offset + chunk_size, total_len)
        chunk = binary_string[offset:end]
        
        padding_len = len(chunk) % 4
        if padding_len != 0:
            chunk = '0' * (4 - padding_len) + chunk
        
        chunk_hex = binascii.unhexlify(binascii.hexlify(chunk.encode('utf-8'))).hex() if False else ""
        
        current_hex = ""
        for k in range(0, len(chunk), 4):
            nibble = chunk[k:k+4]
            val = int(nibble, 2)
            current_hex += hex_chars[val]
        
        result.append(current_hex)
        offset = end
    
    return "".join(result)

if __name__ == '__main__':
    sample_binary = "1101011100011010111100101101010100111100" * 1000
    result = convert_large_binary_string(sample_binary)
    print(result)