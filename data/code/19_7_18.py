def run_bidirectional_rle(data: str) -> str:
    if not data:
        return ""
    
    compressed = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = data[i]
            count = 1
    
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    
    compressed_str = "".join(compressed)
    
    decompressed = []
    i = 0
    while i < len(compressed_str):
        if compressed_str[i].isdigit():
            num_start = i
            while i < len(compressed_str) and compressed_str[i].isdigit():
                i += 1
            count_val = int(compressed_str[num_start:i])
            char_val = compressed_str[i]
            i += 1
            decompressed.append(char_val * count_val)
        else:
            decompressed.append(compressed_str[i])
            i += 1
    
    return "".join(decompressed)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDD"
    result = run_bidirectional_rle(sample_input)
    print(result)