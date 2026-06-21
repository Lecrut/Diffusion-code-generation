def compress_run_length(s):
    if not s:
        return ""
    
    if len(s) < 2:
        return s
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = char
            count = 1
    
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    sample_string = "aabcccccaaa"
    compressed = compress_run_length(sample_string)
    print(compressed)
    
    empty_input = ""
    compressed_empty = compress_run_length(empty_input)
    print(compressed_empty)
    
    single_char = "z"
    compressed_single = compress_run_length(single_char)
    print(compressed_single)
    
    no_run_input = "abc"
    compressed_no_run = compress_run_length(no_run_input)
    print(compressed_no_run)