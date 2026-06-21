def large_binary_to_hex(binary_str):
    if not isinstance(binary_str, str):
        raise TypeError("Input must be a string")
    
    length = len(binary_str)
    if length == 0:
        return ""
    
    if length % 8 != 0:
        padded = binary_str.zfill((length // 8 + 1) * 8)
    else:
        padded = binary_str
    
    num_chunks = len(padded) // 8
    hex_chars = []
    
    for i in range(num_chunks):
        chunk = padded[i * 8 : (i + 1) * 8]
        byte_val = int(chunk, 2)
        hex_chars.append(f"{byte_val:02x}")
    
    result = "".join(hex_chars)
    if len(result) > 0 and result[0] == '0':
        start_index = 1
        while start_index < len(result) and result[start_index] == '0':
            start_index += 1
        if start_index == len(result):
            return "0"
        result = result[start_index:]
        
    return result

if __name__ == '__main__':
    binary_sample = "11110000101010101100110011111111"
    hex_result = large_binary_to_hex(binary_sample)
    print(hex_result)