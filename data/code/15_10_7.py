def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char + str(count))
    
    result = "".join(compressed)
    return result if len(result) < len(s) else s

if __name__ == "__main__":
    sample_input = "aaabbccdddd"
    print(compress_string(sample_input))
    
    sample_input_2 = "abcd"
    print(compress_string(sample_input_2))
    
    sample_input_3 = "aaaaa"
    print(compress_string(sample_input_3))
    
    sample_input_4 = ""
    print(compress_string(sample_input_4))