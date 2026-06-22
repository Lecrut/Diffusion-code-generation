def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char + str(count))
    
    return "".join(compressed)

if __name__ == "__main__":
    test_cases = [
        "aabcccccaaa",
        "",
        "abcdef",
        "a",
        "AAABBBCCCC",
        "1223334444"
    ]
    
    for test in test_cases:
        result = compress_string(test)
        print(result)