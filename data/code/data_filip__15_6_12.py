def compress_sequence(sequence):
    if not sequence:
        return
    current_char = sequence[0]
    count = 1
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            yield current_char, count
            current_char = char
            count = 1
    yield current_char, count

if __name__ == '__main__':
    sample_data = 'zzzzzxyyy'
    result = list(compress_sequence(sample_data))
    print(result)