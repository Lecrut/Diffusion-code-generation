def run_length_encode(text):
    if not text:
        return
    count = 1
    current_char = text[0]
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)

if __name__ == '__main__':
    sample_input = "aaabbaaac"
    result = list(run_length_encode(sample_input))
    print(result)