def run_length_encode(text):
    if not text:
        return

    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1

    yield (current_char, count)

if __name__ == '__main__':
    sample = "AAABBBCCD"
    encoded = list(run_length_encode(sample))
    print(encoded)

    sample_empty = ""
    encoded_empty = list(run_length_encode(sample_empty))
    print(encoded_empty)

    sample_single = "A"
    encoded_single = list(run_length_encode(sample_single))
    print(encoded_single)

    sample_mixed = "ABCABC"
    encoded_mixed = list(run_length_encode(sample_mixed))
    print(encoded_mixed)