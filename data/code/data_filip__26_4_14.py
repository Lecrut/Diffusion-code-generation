def run_length_encode(text):
    if not text:
        return ""
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            yield str(count) + current_char
            current_char = char
            count = 1
    yield str(count) + current_char

def encode_string(text):
    return "".join(run_length_encode(text))

if __name__ == '__main__':
    sample_input = "AAABBBCCDAAA"
    result = encode_string(sample_input)
    print(result)