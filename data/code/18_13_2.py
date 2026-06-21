def run_length_encode(data):
    if not data:
        return
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)

def run_length_decode(encoded_data):
    for char, count in encoded_data:
        for _ in range(count):
            yield char

if __name__ == '__main__':
    sample_input = "aaabbccccdddd"
    encoded = list(run_length_encode(sample_input))
    decoded = "".join(run_length_decode(encoded))
    print(encoded)
    print(decoded)