import sys

def binary_to_hex_chunked(binary_string, chunk_size=64):
    if not binary_string:
        return ""
    if any(c not in '01' for c in binary_string):
        raise ValueError("Input contains non-binary characters")
    hex_chunks = []
    for i in range(0, len(binary_string), chunk_size):
        chunk = binary_string[i : i + chunk_size]
        decimal_val = int(chunk, 2)
        hex_val = hex(decimal_val)[2:]
        if i == 0 and len(binary_string) > chunk_size:
            hex_chunks.append(hex_val)
        elif i == 0:
            hex_chunks.append(hex_val)
        else:
            pad_len = (chunk_size // 4) - len(hex_val)
            hex_chunks.append(hex_val.zfill(pad_len))
    return ''.join(hex_chunks)

if __name__ == '__main__':
    sample_binary = "1101011110011100101100001111111100001111000011111111000011111111"
    result = binary_to_hex_chunked(sample_binary)
    print(result)