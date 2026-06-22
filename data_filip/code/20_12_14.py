def run_length_encode(sequence):
    if not sequence:
        return {}
    counts = {}
    current_char = sequence[0]
    current_count = 0
    for char in sequence:
        if char == current_char:
            current_count += 1
        else:
            if current_char in counts:
                counts[current_char] += current_count
            else:
                counts[current_char] = current_count
            current_char = char
            current_count = 1
    if current_char in counts:
        counts[current_char] += current_count
    else:
        counts[current_char] = current_count
    return counts

if __name__ == '__main__':
    sample_data = "aaabbcdddddeee"
    result = run_length_encode(sample_data)
    print(result)