def run_length_encode(chars):
    if not chars:
        return []
    result = []
    current_char = chars[0]
    count = 1
    for i in range(1, len(chars)):
        if chars[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = chars[i]
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    characters = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c']
    encoded = run_length_encode(characters)
    print(encoded)