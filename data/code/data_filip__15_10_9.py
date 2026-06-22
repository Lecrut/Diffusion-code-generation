def compress_string(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
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
    
    if len(compressed) >= len(s):
        return s
    
    return compressed

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    output = compress_string(sample_input)
    print(output)
    
    sample_input_long = "aaaa"
    output_long = compress_string(sample_input_long)
    print(output_long)
    
    sample_input_no_repeat = "abcdef"
    output_no_repeat = compress_string(sample_input_no_repeat)
    print(output_no_repeat)
    
    sample_input_empty = ""
    output_empty = compress_string(sample_input_empty)
    print(output_empty)