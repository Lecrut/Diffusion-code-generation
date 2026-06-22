def compress_string(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    sample_input = "wwwwaaadexxxxxx"
    compressed = compress_string(sample_input)
    print(compressed)