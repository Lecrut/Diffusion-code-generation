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
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    
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
        num_str = ""
        while i < n and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        
        if num_str:
            count = int(num_str)
        else:
            count = 1
        
        if i < n:
            char = encoded[i]
            i += 1
            decoded.append(char * count)
        else:
            break
    
    return "".join(decoded)

if __name__ == '__main__':
    sample_strings = [
        "aabbbcccc",
        "aaaaaaaa",
        "abc",
        "aabbccdd",
        "",
        "xyyzz",
        "aaabbbcccdddd",
        "hello",
        "111222333",
        "abcdefg"
    ]
    
    for s in sample_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {s!r}")
        print(f"Encoded:  {encoded!r}")
        print(f"Decoded:  {decoded!r}")
        print(f"Match:    {s == decoded}")
        print()