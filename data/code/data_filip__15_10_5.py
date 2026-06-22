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
            if count > 1:
                result.append(current_char)
                result.append(str(count))
            else:
                result.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        result.append(current_char)
        result.append(str(count))
    else:
        result.append(current_char)
    
    compressed = "".join(result)
    if len(compressed) < len(s):
        return compressed
    else:
        return s

if __name__ == '__main__':
    samples = [
        "aaabbbcc",
        "abcdef",
        "aabbccdd",
        "aaaaa",
        "",
        "a"
    ]
    
    for sample in samples:
        print(compress_string(sample))