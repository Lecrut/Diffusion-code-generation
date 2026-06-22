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
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

if __name__ == '__main__':
    sample_sequence = 'wwwwaaadexxxxxx'
    result = compress_sequence(sample_sequence)
    print(result)