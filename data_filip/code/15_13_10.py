def compress_string(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    length = len(data)
    
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(data[i - 1])
            result.append(str(count))
            count = 1
    
    result.append(data[-1])
    result.append(str(count))
    
    final_compressed = "".join(result)
    
    if len(final_compressed) >= length:
        return data
    
    return final_compressed

if __name__ == '__main__':
    sample_input = "aaabbbccccdddddddddddddd"
    compressed_output = compress_string(sample_input)
    print(compressed_output)
    
    sample_input_2 = "abcdef"
    compressed_output_2 = compress_string(sample_input_2)
    print(compressed_output_2)