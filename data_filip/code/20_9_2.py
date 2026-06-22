def run_length_encode(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a', 'a', 'a']
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)