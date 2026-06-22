def run_length_encode(sequence):
    if not sequence:
        return {}
    result = {}
    current_char = sequence[0]
    count = 1
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            result[current_char] = result.get(current_char, 0) + count
            current_char = char
            count = 1
    result[current_char] = result.get(current_char, 0) + count
    return result

if __name__ == '__main__':
    sample_sequence = "aaabbccccd"
    encoded_result = run_length_encode(sample_sequence)
    print(encoded_result)