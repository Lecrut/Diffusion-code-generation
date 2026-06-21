def run_length_encode(sequence):
    if not sequence:
        return []
    
    result = []
    current_char = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = sequence[i]
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_sequence = "AAABBBCCD"
    encoded = run_length_encode(sample_sequence)
    print(encoded)
    
    another_sequence = "ABBCDDDEEEEE"
    encoded2 = run_length_encode(another_sequence)
    print(encoded2)
    
    empty_sequence = ""
    encoded3 = run_length_encode(empty_sequence)
    print(encoded3)
    
    single_char = "A"
    encoded4 = run_length_encode(single_char)
    print(encoded4)