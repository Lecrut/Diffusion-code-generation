def compress_string(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    length = len(s)
    
    for i in range(1, length):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    
    compressed = "".join(result)
    
    if len(compressed) >= length:
        return s
    
    return compressed

if __name__ == '__main__':
    test_input = "aaabbc"
    print(compress_string(test_input))
    
    test_input2 = "abc"
    print(compress_string(test_input2))
    
    test_input3 = "aaaaa"
    print(compress_string(test_input3))
    
    test_input4 = "ababababab"
    print(compress_string(test_input4))