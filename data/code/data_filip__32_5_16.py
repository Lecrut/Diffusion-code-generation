import sys

def binary_to_hex_chunked(binary_str: str) -> str:
    chunk_size = 131072
    total_chunks = (len(binary_str) + chunk_size - 1) // chunk_size
    result_parts = []
    
    for i in range(total_chunks):
        start = i * chunk_size
        end = start + chunk_size
        chunk = binary_str[start:end]
        hex_val = hex(int(chunk, 2))[2:].upper()
        if i < total_chunks - 1:
            target_len = (chunk_size // 4)
            hex_val = hex_val.zfill(target_len)
        result_parts.append(hex_val)
    
    return "".join(result_parts)

if __name__ == '__main__':
    sample_binary = "1111000010101011110011011110111100001010101111001101111011110000101010111100110111101111"
    result = binary_to_hex_chunked(sample_binary)
    print(result)