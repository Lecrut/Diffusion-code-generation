def compress_sequence(sequence):
    if not sequence:
        return ""
    
    result = []
    count = 1
    current_char = sequence[0]
    
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = char
            count = 1
            
    result.append(current_char)
    result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = 'wwwwaaadexxxxxx'
    compressed = compress_sequence(sample_input)
    print(compressed)