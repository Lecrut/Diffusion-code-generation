def compress_sequence(s: str) -> str:
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
    
    return s if len(compressed) >= len(s) else compressed

if __name__ == '__main__':
    print(compress_sequence("aaabbc"))
    print(compress_sequence("abc"))
    print(compress_sequence("aabbccdd"))
    print(compress_sequence("abab"))
    print(compress_sequence(""))
    print(compress_sequence("aaaaaa"))