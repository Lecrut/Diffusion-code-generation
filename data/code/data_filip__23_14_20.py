def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    test_strings = ["aaabbcccc", "abc", "", "a", "aaabbbccc"]
    for test_str in test_strings:
        encoded = run_length_encode(test_str)
        print(encoded)