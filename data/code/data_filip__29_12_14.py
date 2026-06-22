def run_length_encode_segment_generator(text):
    if not text:
        return
    count = 1
    current_char = text[0]
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if count > 1:
                yield f"{count}{current_char}"
            else:
                yield current_char
            current_char = text[i]
            count = 1
    if count > 1:
        yield f"{count}{current_char}"
    else:
        yield current_char

if __name__ == '__main__':
    sample_string = "aaabbcccc"
    encoded_segments = list(run_length_encode_segment_generator(sample_string))
    print("".join(encoded_segments))