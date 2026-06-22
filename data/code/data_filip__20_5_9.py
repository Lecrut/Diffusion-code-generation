def run_length_encode(char_list):
    if not char_list:
        return []
    encoded = []
    current_char = char_list[0]
    count = 1
    for char in char_list[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_chars = ['a', 'a', 'b', 'c', 'c', 'c', 'd']
    result = run_length_encode(sample_chars)
    print(result)