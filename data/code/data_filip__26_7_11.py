def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = [
        "AAAABBBCCDAA",
        "ABC",
        "AAAAAAAAAA",
        "",
        "AABBCCDD",
        "XYZZZZZXYZ"
    ]
    
    for test_string in sample_strings:
        encoded = run_length_encode(test_string)
        print(f"Input: '{test_string}' -> Output: '{encoded}'")