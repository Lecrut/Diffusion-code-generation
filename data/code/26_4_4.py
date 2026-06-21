def encode_rle(text):
    if not text:
        return ""
    result = []
    iterator = iter(text)
    current_char = next(iterator)
    count = 1
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    encoded_result = encode_rle(sample_input)
    print(encoded_result)