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

if __name__ == '__main__':
    input_list = [1, 1, 1, 2, 3, 3, 2, 2, 1]
    result = run_length_encode(input_list)
    print(result)