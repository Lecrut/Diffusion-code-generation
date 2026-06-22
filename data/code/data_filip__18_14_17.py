def run_length_encode(data):
    if not data:
        return
    count = 1
    previous_char = data[0]
    for current_char in data[1:]:
        if current_char == previous_char:
            count += 1
        else:
            yield (previous_char, count)
            previous_char = current_char
            count = 1
    yield (previous_char, count)

if __name__ == '__main__':
    input_string = "aaabbc"
    encoded_data = list(run_length_encode(input_string))
    print(encoded_data)