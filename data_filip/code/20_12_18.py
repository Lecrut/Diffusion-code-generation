def run_length_encode(sequence):
    if not sequence:
        return {}
    encoded = {}
    current_char = sequence[0]
    current_count = 1
    for char in sequence[1:]:
        if char == current_char:
            current_count += 1
        else:
            encoded[current_char] = encoded.get(current_char, 0) + current_count
            current_char = char
            current_count = 1
    encoded[current_char] = encoded.get(current_char, 0) + current_count
    return encoded

if __name__ == '__main__':
    sample_sequence = "aaabbbaaccccc"
    result = run_length_encode(sample_sequence)
    print(result)