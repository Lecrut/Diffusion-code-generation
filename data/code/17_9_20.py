def run_length_encode(s):
    if not s:
        return ""
    
    encoded_parts = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded_parts.append(current_char)
            encoded_parts.append(str(count))
            current_char = s[i]
            count = 1
    
    encoded_parts.append(current_char)
    encoded_parts.append(str(count))
    
    return ''.join(encoded_parts)

if __name__ == '__main__':
    samples = [
        "",
        "A",
        "AAA",
        "AABBCC",
        "AAABBBCCC",
        "ABCDE",
        "AAABBBCCAAA",
        "112233",
        "aabbccddd",
        "Hello World!!!"
    ]
    
    for sample in samples:
        result = run_length_encode(sample)
        print(f"'{sample}' -> '{result}'")