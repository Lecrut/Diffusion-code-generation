def run_length_encode(characters):
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
    sample_chars = ['a', 'a', 'b', 'b', 'b', 'c', 'a']
    compressed = run_length_encode(sample_chars)
    print(compressed)