def run_length_encode(text):
    if not text:
        return
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            yield f"{count}{current_char}"
            current_char = char
            count = 1
    yield f"{count}{current_char}"

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    encoded = run_length_encode(sample_string)
    result = "".join(encoded)
    print(result)