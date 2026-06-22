def compress_repeated_sequences(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    length = len(s)
    
    for i in range(1, length):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    
    return "".join(compressed)

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = compress_repeated_sequences(sample_input)
    print(result)