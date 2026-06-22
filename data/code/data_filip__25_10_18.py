def compress_string(input_str):
    if not input_str:
        return ""
    
    compressed = []
    count = 1
    n = len(input_str)
    
    for i in range(1, n):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            compressed.append(input_str[i - 1] + str(count))
            count = 1
    
    compressed.append(input_str[-1] + str(count))
    
    result = "".join(compressed)
    
    if len(result) >= len(input_str):
        return input_str
    
    return result

if __name__ == '__main__':
    sample_data = "AAABBBCCDEEEE"
    output = compress_string(sample_data)
    print(output)
    
    empty_data = ""
    print(compress_string(empty_data))
    
    single_char = "A"
    print(compress_string(single_char))
    
    mixed_chars = "AABBAABBCC"
    print(compress_string(mixed_chars))