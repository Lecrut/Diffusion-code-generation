def compress_sequence(seq):
    if not seq:
        return ""
    
    result = []
    count = 1
    current_char = seq[0]
    
    for i in range(1, len(seq)):
        if seq[i] == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = seq[i]
            count = 1
    result.append(current_char + str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_sequence = "wwwwaaadexxxxxx"
    compressed = compress_sequence(sample_sequence)
    print(compressed)