def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    
    encoded.append(str(count) + current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    test_cases = ["", "a", "aa", "aabbc", "aaabbbccccdd", "aabbccdd", "a1b2c3"]
    for text in test_cases:
        print(run_length_encode(text))