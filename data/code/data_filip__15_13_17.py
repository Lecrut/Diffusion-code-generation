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
            if count > 1:
                result.append(str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccddee"
    compressed_result = compress_string(sample_input)
    print(compressed_result)
    
    another_sample = "aabbcc"
    another_result = compress_string(another_sample)
    print(another_result)
    
    empty_sample = ""
    empty_result = compress_string(empty_sample)
    print(empty_result)
    
    single_char_sample = "z"
    single_char_result = compress_string(single_char_sample)
    print(single_char_result)
    
    mixed_sample = "aaaaabbbbcccccccddd"
    mixed_result = compress_string(mixed_sample)
    print(mixed_result)