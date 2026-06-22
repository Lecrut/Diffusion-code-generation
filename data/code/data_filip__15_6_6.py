def run_length_encode_generator(char_sequence):
    if not char_sequence:
        return
    current_char = char_sequence[0]
    count = 1
    for next_char in char_sequence[1:]:
        if next_char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = next_char
            count = 1
    yield (current_char, count)

if __name__ == '__main__':
    sequence = 'zzzzzxyyy'
    encoded = list(run_length_encode_generator(sequence))
    print(encoded)