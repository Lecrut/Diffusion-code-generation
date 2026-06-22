def run_length_encode(s):
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char + str(count))
    
    return "".join(compressed)

if __name__ == '__main__':
    test_cases = [
        "",
        "a",
        "aaa",
        "aabbbcc",
        "aabbcc",
        "abcdef",
        "aaabbaac",
        "a11bb22",
        "Hello World",
        "AAAAAAAAAAAA"
    ]
    
    for test in test_cases:
        result = run_length_encode(test)
        print(result)