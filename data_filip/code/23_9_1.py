def run_length_encode(s):
    if not s:
        return ""
    
    encoded_parts = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded_parts.append(str(count))
            encoded_parts.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded_parts.append(str(count))
    encoded_parts.append(current_char)
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCD",
        "ABC",
        "AAAAA",
        "AABBCC",
        "ABABAB",
        "",
        "A"
    ]
    
    for s in sample_strings:
        result = run_length_encode(s)
        print(f"{repr(s)} -> {repr(result)}")