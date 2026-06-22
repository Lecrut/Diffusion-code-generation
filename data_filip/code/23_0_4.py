def rle_encode(s: str) -> str:
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
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    
    compressed = "".join(result)
    
    if len(compressed) >= len(s):
        return s
    
    return compressed

if __name__ == '__main__':
    test_strings = [
        "AAAABBBCCDAA",
        "",
        "ABC",
        "AAAA",
        "AAB",
        "aabbbcccc"
    ]
    
    for s in test_strings:
        print(rle_encode(s))