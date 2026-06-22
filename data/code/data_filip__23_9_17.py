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
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

def run_length_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        count = ""
        while i < len(encoded) and encoded[i].isdigit():
            count += encoded[i]
            i += 1
        if not count:
            count = 1
        else:
            count = int(count)
        
        if i < len(encoded):
            char = encoded[i]
            decoded.append(char * count)
            i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    test_cases = [
        "AAAABBBCCDAA",
        "A",
        "ABCD",
        "AAAAAA",
        "AABBCCDD",
        "",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    ]
    
    for test in test_cases:
        encoded = run_length_encode(test)
        decoded = run_length_decode(encoded)
        print(f"Original:  {test}")
        print(f"Encoded:   {encoded}")
        print(f"Decoded:   {decoded}")
        print(f"Match:     {test == decoded}")
        print()