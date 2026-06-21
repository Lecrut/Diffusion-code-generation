def run_length_encode(data):
    if not data:
        return ""
    result_parts = []
    segment_start_index = 0
    index = 0
    length = len(data)
    while index < length:
        next_index = index + 1
        while next_index < length and data[next_index] == data[index]:
            next_index += 1
        run_length = next_index - index
        character = data[index]
        if run_length > 1:
            length_str = str(run_length)
            result_parts.append(length_str)
        result_parts.append(character)
        index = next_index
    return "".join(result_parts)

if __name__ == '__main__':
    test_data = "aaabbbcccc"
    encoded_string = run_length_encode(test_data)
    print(encoded_string)