def encode_compressed(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    print(encode_compressed("aaabbbccdaa"))
    print(encode_compressed("abc"))
    print(encode_compressed(""))