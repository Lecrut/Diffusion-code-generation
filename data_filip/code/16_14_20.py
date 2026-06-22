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
            result.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    
    result.append(str(count) + current_char)
    
    return "".join(result)

def run_length_decode(encoded):
    if not encoded:
        return ""
    
    result = []
    i = 0
    n = len(encoded)
    
    while i < n:
        num_str = ""
        while i < n and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        
        if i < n:
            char = encoded[i]
            i += 1
            count = int(num_str) if num_str else 1
            result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    test_strings = [
        "AABBBCCCC",
        "hello world",
        "AAAAABBBBBBBBBBCCCCCCCCCCC",
        "xyzxyzxyz",
        "",
        "A",
        "AAABBBCCC",
        "123123123",
    ]
    
    for s in test_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {s!r}")
        print(f"Encoded:  {encoded!r}")
        print(f"Decoded:  {decoded!r}")
        print(f"Match:    {s == decoded}")
        print()