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
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

def run_length_decode(encoded):
    if not encoded:
        return ""
    
    decoded = []
    i = 0
    n = len(encoded)
    
    while i < n:
        if encoded[i].isdigit():
            count = 0
            while i < n and encoded[i].isdigit():
                count = count * 10 + int(encoded[i])
                i += 1
            if i < n:
                char = encoded[i]
                decoded.append(char * count)
                i += 1
        else:
            decoded.append(encoded[i])
            i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    test_strings = [
        "",
        "A",
        "AAA",
        "AAB",
        "AAABBBCC",
        "AAABBBCCCDD",
        "AAABBBCCCCDDD",
        "AABBCCDDEEFFGGHH",
        "AAAAAAAAAA",
        "ABCDEF",
        "A123B456C",
        "XXYYZZ",
        "XYYZZZ",
        "AAAABBBCCDDDD",
        "W3(m2)2",
        "abcd",
        "aaabbbbcc",
    ]
    
    for s in test_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {repr(s)}")
        print(f"Encoded:  {repr(encoded)}")
        print(f"Decoded:  {repr(decoded)}")
        print(f"Match:    {s == decoded}")
        print()