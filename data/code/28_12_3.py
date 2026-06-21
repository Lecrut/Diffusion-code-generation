def run_length_compress(characters):
    if not characters:
        return []

    compressed = []
    current_char = characters[0]
    count = 1

    for i in range(1, len(characters)):
        if characters[i] == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = characters[i]
            count = 1

    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample1 = ['a', 'a', 'b', 'b', 'b', 'c', 'a']
    print(run_length_compress(sample1))

    sample2 = ['x', 'x', 'x', 'x']
    print(run_length_compress(sample2))

    sample3 = []
    print(run_length_compress(sample3))

    sample4 = ['a', 'b', 'c', 'd', 'e']
    print(run_length_compress(sample4))

    sample5 = ['z']
    print(run_length_compress(sample5))