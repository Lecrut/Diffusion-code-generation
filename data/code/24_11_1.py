def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    sample_strings = [
        "aabbbcccc",
        "hello",
        "aaaaa",
        "abcdef",
        "aabbcc",
        "",
        "a",
        "aaabbbcccaaa"
    ]
    
    for test_string in sample_strings:
        result = run_length_encode(test_string)
        print(result)