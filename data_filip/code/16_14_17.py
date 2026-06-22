def run_length_encode(s):
    if not s:
        return ''
    parts = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                parts.append(str(count))
            parts.append(current_char)
            current_char = s[i]
            count = 1
    if count > 1:
        parts.append(str(count))
    parts.append(current_char)
    return ''.join(parts)

def run_length_decode(s):
    if not s:
        return ''
    parts = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            count = int(s[i:j])
            char = s[j]
            parts.append(char * count)
            i = j + 1
        else:
            parts.append(s[i])
            i += 1
    return ''.join(parts)

if __name__ == '__main__':
    test_strings = [
        'aabbbcccc',
        'hello',
        'a',
        '',
        'aaabbbccc',
        'abcdef',
        'aabbccdd'
    ]
    
    for s in test_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(f"Original: {repr(s)}")
        print(f"Encoded:  {repr(encoded)}")
        print(f"Decoded:  {repr(decoded)}")
        print(f"Match:    {s == decoded}")
        print()