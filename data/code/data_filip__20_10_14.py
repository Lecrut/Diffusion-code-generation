def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    encoded_parts = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded_parts.append(str(count))
            encoded_parts.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        encoded_parts.append(str(count))
    encoded_parts.append(current_char)
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_strings = [
        "AABBCCC",
        "Hello",
        "AAAAAAAAA",
        "XYZ",
        "A",
        "",
        "AAABBBCCCDDD",
        "ABABAB",
        "Mississippi",
        "111222333",
    ]
    
    for test_str in sample_strings:
        result = run_length_encode(test_str)
        print(result)