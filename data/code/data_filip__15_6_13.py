def compress_repeated_chars(sequence):
    if not sequence:
        return []

    result = []
    current_char = sequence[0]
    count = 1

    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1

    result.append((current_char, count))
    return result

def compress_repeated_chars_gen(sequence):
    if not sequence:
        return

    current_char = sequence[0]
    count = 1

    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1

    yield (current_char, count)

if __name__ == '__main__':
    sample_sequence = 'zzzzzxyyy'
    compressed_result = compress_repeated_chars(sample_sequence)
    print(compressed_result)

    compressed_gen_result = list(compress_repeated_chars_gen(sample_sequence))
    print(compressed_gen_result)