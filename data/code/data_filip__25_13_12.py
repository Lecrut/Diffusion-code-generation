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
    return "".join(result)

def run_length_decode(encoded):
    if not encoded:
        return ""
    
    result = []
    i = 0
    while i < len(encoded):
        count = ""
        while i < len(encoded) and encoded[i].isdigit():
            count += encoded[i]
            i += 1
        
        if i < len(encoded):
            char = encoded[i]
            i += 1
            result.append(char * int(count))
    
    return "".join(result)

if __name__ == '__main__':
    test_strings = [
        "aaabbc",
        "aabcccccaaa",
        "abcdef",
        "",
        "a",
        "aaaaaaaaaaaaaaaaaaaa",
        "AABBCCDD"
    ]
    
    for s in test_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {s!r}")
        print(f"Encoded:  {encoded!r}")
        print(f"Decoded:  {decoded!r}")
        print(f"Match:    {s == decoded}")
        print()