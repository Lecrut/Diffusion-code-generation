def rle_encode(text):
    if not text:
        return ""
    encoded_chars = []
    count = 1
    padded = text + '\0'
    for char, next_char in zip(text, padded):
        if char == next_char:
            count += 1
        else:
            encoded_chars.append(char)
            if count > 1:
                encoded_chars.append(str(count))
            count = 1
    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_input = 'AAAAABBBB'
    print(rle_encode(sample_input))