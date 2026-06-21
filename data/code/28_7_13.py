def run_length_encode(text):
    if not text:
        return
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            yield current_char * count if count > 1 else current_char
            current_char = char
            count = 1
    yield current_char * count if count > 1 else current_char

def encode_string(text):
    return "".join(run_length_encode(text))

if __name__ == '__main__':
    sample1 = "AAAABBBCCDAA"
    print(encode_string(sample1))
    sample2 = "ABC"
    print(encode_string(sample2))
    sample3 = "A"
    print(encode_string(sample3))
    sample4 = ""
    print(encode_string(sample4))