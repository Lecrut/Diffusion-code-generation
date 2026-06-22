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

if __name__ == '__main__':
    sample_input = "aaabbcdddd"
    result = list(run_length_encode(sample_input))
    print(result)