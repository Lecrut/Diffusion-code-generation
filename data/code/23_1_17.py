def run_length_encode(data):
    if not data:
        return []
    result = []
    if len(data) == 1:
        return [(data[0], 1)]
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

def run_length_decode(encoded_data):
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)