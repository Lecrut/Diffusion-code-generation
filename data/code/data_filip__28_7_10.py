def rle_encode(text):
    if not text:
        return
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            yield current_char, count
            current_char = char
            count = 1
    yield current_char, count

def rle_decode(encoded_tuples):
    for char, count in encoded_tuples:
        yield char * count

if __name__ == '__main__':
    sample_text = "aaabbbcccaaa"
    encoded = list(rle_encode(sample_text))
    decoded = "".join(rle_decode(encoded))
    print(encoded)
    print(decoded)