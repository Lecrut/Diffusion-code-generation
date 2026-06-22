def run_length_encode(sequence):
    if not sequence:
        return ""
    encoded = []
    current_char = sequence[0]
    count = 1
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    sample_sequence = "aaabbbcccaad"
    result = run_length_encode(sample_sequence)
    print(result)