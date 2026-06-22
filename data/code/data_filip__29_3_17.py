def encode_consecutive_duplicates(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = s[i]
            count = 1
    
    encoded.append(current_char)
    encoded.append(str(count))
    
    return "".join(encoded)

if __name__ == '__main__':
    test_cases = [
        "aabbc",
        "hello",
        "aaabbbccc",
        "abcdef",
        "a",
        ""
    ]
    
    for test in test_cases:
        result = encode_consecutive_duplicates(test)
        print(f"Input: '{test}' -> Output: '{result}'")