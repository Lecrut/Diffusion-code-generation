def rle_encode(text):
    if not text:
        return ""

    encoded = []
    current_char = text[0]
    count = 1
    length = len(text)
    index = 1

    while index < length:
        char = text[index]
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
        index += 1

    encoded.append(str(count))
    encoded.append(current_char)

    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    result = rle_encode(sample_string)
    print(result)