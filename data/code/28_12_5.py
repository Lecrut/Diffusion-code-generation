def run_length_compress(characters):
    if not characters:
        return []

    result = []
    current_char = characters[0]
    count = 1

    for char in characters[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1

    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample1 = ['a', 'a', 'b', 'b', 'b', 'c']
    print(run_length_compress(sample1))

    sample2 = ['x', 'y', 'z']
    print(run_length_compress(sample2))

    sample3 = []
    print(run_length_compress(sample3))

    sample4 = ['a', 'a', 'a', 'a']
    print(run_length_compress(sample4))