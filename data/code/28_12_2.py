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
    sample = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a']
    print(run_length_compress(sample))

    sample_empty = []
    print(run_length_compress(sample_empty))

    sample_single = ['x']
    print(run_length_compress(sample_single))

    sample_all_same = ['z', 'z', 'z', 'z']
    print(run_length_compress(sample_all_same))

    sample_no_repeats = ['a', 'b', 'c', 'd']
    print(run_length_compress(sample_no_repeats))