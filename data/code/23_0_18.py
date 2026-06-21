def run_length_encode(s: str) -> str:
    if not s:
        return s
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return ''.join(encoded)

if __name__ == '__main__':
    test_strings = [
        "",
        "a",
        "aa",
        "abc",
        "aabbccc",
        "aabcccccaaa",
        "xyz"
    ]
    
    for s in test_strings:
        result = run_length_encode(s)
        print(result)