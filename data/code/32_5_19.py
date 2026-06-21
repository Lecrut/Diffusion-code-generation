import sys

def binary_to_hex_chunked(bin_str: str, chunk_size: int = 64) -> str:
    if not bin_str:
        return ""
    
    bin_str = bin_str.strip()
    
    if not all(c in '01' for c in bin_str):
        raise ValueError("Input string contains non-binary characters")
    
    pad_len = len(bin_str) % 4
    if pad_len != 0:
        bin_str = '0' * (4 - pad_len) + bin_str
    
    hex_chars = "0123456789ABCDEF"
    
    chunk_size = min(chunk_size, len(bin_str))
    
    hex_result = []
    for i in range(0, len(bin_str), chunk_size):
        chunk = bin_str[i : i + chunk_size]
        chunk_len = len(chunk)
        
        if chunk_len > 4:
            hex_chunk = []
            for j in range(0, chunk_len, 4):
                nibble = chunk[j : j+4]
                val = 0
                for k in range(4):
                    val = (val << 1) | (1 if nibble[k] == '1' else 0)
                hex_chunk.append(hex_chars[val])
            hex_result.append("".join(hex_chunk))
        else:
            val = 0
            for k in range(chunk_len):
                val = (val << 1) | (1 if chunk[k] == '1' else 0)
            hex_result.append(hex_chars[val])
    
    return "".join(hex_result)

if __name__ == '__main__':
    sample_binary = "11110000101010101100110011110000" * 1000
    result = binary_to_hex_chunked(sample_binary)
    print(result[:64])