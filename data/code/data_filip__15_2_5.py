def compress(sequence):
    if not sequence:
        return ""
    
    compressed = []
    count = 1
    current_char = sequence[0]
    
    for i in range(1, len(sequence)):
        char = sequence[i]
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = char
            count = 1
    
    compressed.append(current_char)
    compressed.append(str(count))
    
    return "".join(compressed)

if __name__ == '__main__':
    sequence = 'wwwwaaadexxxxxx'
    result = compress(sequence)
    print(result)