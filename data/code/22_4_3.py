def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "",
        "A",
        "AA",
        "AAA",
        "AAB",
        "AABBBCC",
        "AABBCC",
        "ABC",
        "AAAAAABBBBBBBBBBBCCCCCCCCCCDDD"
    ]
    
    for test_case in test_cases:
        encoded = run_length_encode(test_case)
        print(f"Input: '{test_case}' -> Output: '{encoded}'")