def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    
    result.append(str(count) + current_char)
    return "".join(result)

def run_length_decode(encoded_s):
    if not encoded_s:
        return ""
    
    result = []
    i = 0
    while i < len(encoded_s):
        count_str = ""
        while i < len(encoded_s) and encoded_s[i].isdigit():
            count_str += encoded_s[i]
            i += 1
        if count_str:
            count = int(count_str)
            char = encoded_s[i]
            result.append(char * count)
            i += 1
        else:
            break
    
    return "".join(result)

if __name__ == "__main__":
    test_cases = [
        "aaabbbcccd",
        "a",
        "abcdef",
        "aaaaa",
        "aabbbcccc",
        "",
        "aabbcc",
        "zzzzzyyyyyxxxx",
    ]
    
    for test in test_cases:
        encoded = run_length_encode(test)
        decoded = run_length_decode(encoded)
        print(f"Original: '{test}'")
        print(f"Encoded:  '{encoded}'")
        print(f"Decoded:  '{decoded}'")
        print(f"Match:    {test == decoded}")
        print()