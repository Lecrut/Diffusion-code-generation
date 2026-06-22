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
    if len(compressed) >= len(s):
        return s
    return compressed

if __name__ == '__main__':
    test_string = "aaabbcdddeee"
    print(compress_string(test_string))