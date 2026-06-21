import binascii

def binary_string_to_hex(bin_str):
    if not bin_str:
        return ''
    
    result = []
    chunk_size = 8
    length = len(bin_str)
    i = 0
    
    while i < length:
        end = min(i + chunk_size, length)
        chunk = bin_str[i:end]
        padding_len = chunk_size - len(chunk)
        if padding_len:
            chunk = chunk + '0' * padding_len
        result.append(hex(int(chunk, 2))[2:].zfill(chunk_size // 2))
        i = end
    
    return ''.join(result)

if __name__ == '__main__':
    sample_bin = '11010101001000110101010100100011'
    hex_result = binary_string_to_hex(sample_bin)
    print(hex_result)