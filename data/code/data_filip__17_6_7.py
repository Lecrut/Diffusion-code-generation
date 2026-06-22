def compress_rle(input_str):
    if not input_str:
        return ""
    
    compressed = []
    count = 1
    length = len(input_str)
    
    for i in range(1, length):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            compressed.append(input_str[i - 1])
            if count > 1:
                compressed.append(str(count))
            count = 1
    
    compressed.append(input_str[-1])
    if count > 1:
        compressed.append(str(count))
    
    result = "".join(compressed)
    
    if len(result) >= len(input_str):
        return input_str
    
    return result

if __name__ == '__main__':
    sample_string = "aaabbc"
    compressed_result = compress_rle(sample_string)
    print(compressed_result)