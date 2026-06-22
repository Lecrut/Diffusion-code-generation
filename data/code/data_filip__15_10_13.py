def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char)
    result.append(str(count))
    
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    sample_input = "aaabbbcccc"
    output = compress_string(sample_input)
    print(output)
    
    sample_input_2 = "abcd"
    output_2 = compress_string(sample_input_2)
    print(output_2)
    
    sample_input_3 = ""
    output_3 = compress_string(sample_input_3)
    print(output_3)
    
    sample_input_4 = "aaaaa"
    output_4 = compress_string(sample_input_4)
    print(output_4)