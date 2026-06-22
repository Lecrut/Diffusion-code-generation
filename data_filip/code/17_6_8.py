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
            compressed.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char + str(count))
    
    result = "".join(compressed)
    
    if len(result) >= len(s):
        return s
    
    return result

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    output = compress_string(sample_input)
    print(output)