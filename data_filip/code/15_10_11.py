def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char)
    compressed.append(str(count))
    
    result = "".join(compressed)
    return result if len(result) < len(s) else s

if __name__ == "__main__":
    sample_input = "aaabbbcccaaa"
    output = compress_string(sample_input)
    print(output)
    
    sample_input_2 = "abcdef"
    output_2 = compress_string(sample_input_2)
    print(output_2)
    
    sample_input_3 = "aaaa"
    output_3 = compress_string(sample_input_3)
    print(output_3)