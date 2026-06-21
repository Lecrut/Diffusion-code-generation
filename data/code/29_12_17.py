def encode_segments(input_string):
    if not input_string:
        return
    current_char = input_string[0]
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            yield f"{current_char}{count}"
            current_char = input_string[i]
            count = 1
    yield f"{current_char}{count}"

if __name__ == '__main__':
    sample_text = "aaabbccccd"
    encoded_segments = list(encode_segments(sample_text))
    print(encoded_segments)