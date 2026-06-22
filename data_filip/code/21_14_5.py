def run_length_encode(sequence):
    if not sequence:
        return []
    
    encoded = []
    current_char = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        char = sequence[i]
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sequence = "aaabbc"
    result = run_length_encode(sequence)
    print(result)