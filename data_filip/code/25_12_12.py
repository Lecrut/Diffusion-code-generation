def run_length_encode(sequence):
    if not sequence:
        return []
    encoded = []
    current_char = sequence[0]
    count = 1
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

def run_length_decode(encoded_sequence):
    decoded = []
    for char, count in encoded_sequence:
        decoded.extend([char] * count)
    return decoded

if __name__ == '__main__':
    original_text = "AAAABBBCCDAA"
    encoded_data = run_length_encode(original_text)
    decoded_data = run_length_decode(encoded_data)