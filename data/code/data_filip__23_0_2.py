def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + (str(count) if count > 1 else ""))
            count = 1
    
    result.append(s[-1] + (str(count) if count > 1 else ""))
    
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "",
        "a",
        "aa",
        "aab",
        "aaabbbcccc",
        "abcdef",
        "1122334455",
        "AABBBCCCCDDDEEE"
    ]
    
    for test in test_cases:
        encoded = run_length_encode(test)
        print(f"Original: '{test}' -> Encoded: '{encoded}'")