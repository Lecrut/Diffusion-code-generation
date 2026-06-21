def compress_sequence(sequence):
    if not sequence:
        return ""
    
    compressed = []
    current_char = sequence[0]
    count = 1
    
    for char in sequence[1:]:
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
    result = compress_sequence('wwwwaaadexxxxxx')
    print(result)