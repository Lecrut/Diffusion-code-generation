def run_length_encode(sequence):
    if not sequence:
        return {}
    result = {}
    current_char = sequence[0]
    count = 0
    for char in sequence:
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample_input = "aaabbc"
    encoded = run_length_encode(sample_input)
    print(encoded)