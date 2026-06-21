def encode(data):
    if not data:
        return []
    result = []
    current_char = data[0]
    count = 1
    for index in range(1, len(data)):
        char = data[index]
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    encoded_result = encode(sample_input)
    print(encoded_result)