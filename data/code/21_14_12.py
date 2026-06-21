def run_length_encoding(sequence):
    if not sequence:
        return []
    
    encoded = []
    current_char = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = sequence[i]
            count = 1
    
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_sequence = "aaabbccccd"
    result = run_length_encoding(sample_sequence)
    print(result)