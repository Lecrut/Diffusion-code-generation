def encode_string(s: str) -> str:
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count == 1:
                result.append(current_char)
            else:
                result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    if count == 1:
        result.append(current_char)
    else:
        result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "",
        "a",
        "aa",
        "aaa",
        "abcdef",
        "aabbcc",
        "aabcccccaaa",
        "1122334455",
        "a1b1c1",
        "AAAaaB"
    ]
    
    for test in test_cases:
        encoded = encode_string(test)
        print(f"Input: '{test}' -> Encoded: '{encoded}'")