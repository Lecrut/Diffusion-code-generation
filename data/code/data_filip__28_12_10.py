def run_length_compress(characters):
    if not characters:
        return []

    compressed = []
    current_char = characters[0]
    count = 1

    for char in characters[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1

    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample_input = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a', 'a', 'a']
    result = run_length_compress(sample_input)
    print(result)

    empty_input = []
    result_empty = run_length_compress(empty_input)
    print(result_empty)

    single_input = ['x']
    result_single = run_length_compress(single_input)
    print(result_single)

    mixed_input = ['m', 'n', 'o', 'p', 'q']
    result_mixed = run_length_compress(mixed_input)
    print(result_mixed)

    all_same_input = ['z', 'z', 'z', 'z', 'z']
    result_all_same = run_length_compress(all_same_input)
    print(result_all_same)