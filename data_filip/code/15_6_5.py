def compress_sequence(sequence):
    if not sequence:
        return
    current_char = sequence[0]
    count = 1
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            yield count, current_char
            current_char = char
            count = 1
    yield count, current_char

if __name__ == '__main__':
    sample_data = 'zzzzzxyyy'
    result = list(compress_sequence(sample_data))
    print(result)