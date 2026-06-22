def rle_encode(text):
    if not text:
        return ""
    encoded = []
    count = 1
    current_char = text[0]
    length = len(text)
    for i in range(1, length):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_text = "aaabbcccc"
    result = rle_encode(sample_text)
    print(result)