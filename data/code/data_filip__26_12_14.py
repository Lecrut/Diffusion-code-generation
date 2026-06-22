def compress_string(s):
    if not s:
        return ""
    if len(s) == 1:
        return s[0] + "1"
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input_1 = "aaabbbcccc"
    sample_input_2 = "abcdef"
    sample_input_3 = ""
    sample_input_4 = "a"
    
    print(compress_string(sample_input_1))
    print(compress_string(sample_input_2))
    print(compress_string(sample_input_3))
    print(compress_string(sample_input_4))