def compress_string(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    
    compressed = "".join(result)
    
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    test_cases = [
        "aabcccccaaa",
        "abcdef",
        "aaaaa",
        "ab",
        "",
        "aaabbcccc",
        "aabbcc"
    ]
    
    for test in test_cases:
        print(compress_string(test))