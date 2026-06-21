def compress_string(s: str) -> str:
    if not s:
        return ""
    
    if len(s) == 1:
        return s
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    result.append(f"{current_char}{count}")
    
    compressed = "".join(result)
    
    if len(compressed) >= len(s):
        return s
    
    return compressed

if __name__ == '__main__':
    sample_input = "aaabbc"
    output = compress_string(sample_input)
    print(output)