def rle_compress(binary_string: str) -> str:
    if not binary_string:
        return ""
    
    compressed = []
    count = 1
    current_char = binary_string[0]
    
    for char in binary_string[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed.append(f"{current_char}{count}")
    
    return "".join(compressed)

def rde_decompress(compressed_string: str) -> str:
    if not compressed_string:
        return ""
    
    decompressed = []
    i = 0
    
    while i < len(compressed_string):
        if i + 1 >= len(compressed_string):
            raise ValueError("Compressed string format is invalid.")
        
        char = compressed_string[i]
        count_str = ""
        j = i + 1
        
        while j < len(compressed_string) and compressed_string[j].isdigit():
            count_str += compressed_string[j]
            j += 1
        
        if not count_str:
            raise ValueError("Compressed string format is invalid: missing count.")
        
        count = int(count_str)
        decompressed.append(char * count)
        i = j
    
    return "".join(decompressed)

if __name__ == '__main__':
    binary_input = '0011100'
    compressed_result = rle_compress(binary_input)
    print(compressed_result)
    decompressed_result = rde_decompress(compressed_result)
    print(decompressed_result)
    
    empty_input = ''
    empty_compressed = rle_compress(empty_input)
    print(empty_compressed)
    
    single_run_input = '11111'
    single_run_compressed = rle_compress(single_run_input)
    print(single_run_compressed)
    
    single_char_input = '1'
    single_char_compressed = rle_compress(single_char_input)
    print(single_char_compressed)
    single_char_decompressed = rde_decompress(single_char_compressed)
    print(single_char_decompressed)