def run_length_encode(sequence):
    encoded = []
    index = 0
    length = len(sequence)
    while index < length:
        current_item = sequence[index]
        run_count = 0
        while index < length and sequence[index] == current_item:
            run_count += 1
            index += 1
        encoded.append((current_item, run_count))
    return encoded

if __name__ == '__main__':
    input_sequence = [7, 7, 7, 8, 8, 9, 10, 10, 10, 10]
    output = run_length_encode(input_sequence)
    print(output)