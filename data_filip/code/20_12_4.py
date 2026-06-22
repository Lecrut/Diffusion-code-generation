def run_length_encode(sequence):
    if not sequence:
        return {}
    counts = {}
    current_char = sequence[0]
    current_count = 1
    for char in sequence[1:]:
        if char == current_char:
            current_count += 1
        else:
            counts[current_char] = current_count
            current_char = char
            current_count = 1
    counts[current_char] = current_count
    return counts

if __name__ == '__main__':
    sample_data = "aaabbbccccddee"
    result = run_length_encode(sample_data)
    print(result)