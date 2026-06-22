def encode_run_length(source):
    if not source:
        return []
    segments = []
    char_buffer = source[0]
    count = 1
    for char in source[1:]:
        if char == char_buffer:
            count += 1
        else:
            segments.append((char_buffer, count))
            char_buffer = char
            count = 1
    segments.append((char_buffer, count))
    return segments

if __name__ == '__main__':
    input_text = 'AAAABBBCCDAA'
    encoded_data = encode_run_length(input_text)
    print(encoded_data)