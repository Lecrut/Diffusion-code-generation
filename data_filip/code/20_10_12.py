def run_length_encode(s):
    if not s:
        return ""
    
    encoded_parts = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(str(count))
            encoded_parts.append(current_char)
            current_char = char
            count = 1
    
    encoded_parts.append(str(count))
    encoded_parts.append(current_char)
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_strings = [
        "AABCCCDD",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        "",
        "A",
        "ABCD",
        "AAABBBCCC"
    ]
    
    for sample in sample_strings:
        result = run_length_encode(sample)
        print(result)