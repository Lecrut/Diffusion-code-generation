def compress_repeated_chars(sequence):
    if not sequence:
        return ""
    
    result = []
    current_char = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(current_char * count)
            else:
                result.append(current_char)
            current_char = sequence[i]
            count = 1
    
    if count > 1:
        result.append(current_char * count)
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_sequence = "zzzzzxyyy"
    compressed = compress_repeated_chars(sample_sequence)
    print(compressed)