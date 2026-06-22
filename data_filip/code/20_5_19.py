def run_length_encode(characters):
    if not characters:
        return []

    encoded = []
    current_char = characters[0]
    count = 1

    for char in characters[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1

    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_characters = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd']
    result = run_length_encode(sample_characters)
    print(result)