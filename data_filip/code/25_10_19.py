def compress_string(input_str):
    if not input_str:
        return ""
    
    result = []
    count = 1
    current_char = input_str[0]
    
    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = input_str[i]
            count = 1
    
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "aabcccccaaa",
        "abc",
        "aabbcc",
        "aaabbcc",
        "",
        "aaa",
        "a",
        "aabbccaa"
    ]
    
    for s in sample_strings:
        compressed = compress_string(s)
        print(compressed)