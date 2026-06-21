def run_length_encoding(chars):
    if not chars:
        return []
    result = []
    current_char = chars[0]
    count = 1
    for char in chars[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_data = ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a']
    print(run_length_encoding(sample_data))