def run_length_encode(s):
    if not s:
        return ""
    if len(s) == 1:
        return s[0] + "1"
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    encoded.append(current_char + str(count))
    return ''.join(encoded)

def run_length_decode(s):
    if not s:
        return ""
    
    decoded = []
    i = 0
    while i < len(s):
        char = s[i]
        j = i + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        count = int(s[i+1:j]) if i+1 < j else 1
        decoded.append(char * count)
        i = j
    
    return ''.join(decoded)

if __name__ == '__main__':
    sample_strings = [
        "",
        "a",
        "aaa",
        "aabbc",
        "aaabbaac",
        "aabbcc",
        "xyzzz",
        "11122233",
        "abcdefghi"
    ]
    
    for s in sample_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: '{s}' -> Encoded: '{encoded}' -> Decoded: '{decoded}'")