import itertools

def rle_encode(text):
    if not text:
        return ""
    encoded = ""
    for char, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        encoded += str(count) + char
    return encoded

if __name__ == '__main__':
    sample_text = "aaabbcdd"
    encoded = rle_encode(sample_text)
    print(encoded)

    empty_text = ""
    encoded_empty = rle_encode(empty_text)
    print(encoded_empty)

    single_char = "z"
    encoded_single = rle_encode(single_char)
    print(encoded_single)

    mixed_text = "hello world"
    encoded_mixed = rle_encode(mixed_text)
    print(encoded_mixed)