def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    test_cases = [
        "",
        "A",
        "ABC",
        "AABBC",
        "AAABBBCCD",
        "AAAAAAAAAA",
        "AABBCCDD",
        "Hello World!!!",
    ]
    
    for test in test_cases:
        result = run_length_encode(test)
        print(f"Input: {repr(test)}")
        print(f"Output: {repr(result)}")
        print()