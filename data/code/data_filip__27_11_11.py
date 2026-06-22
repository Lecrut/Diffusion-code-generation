def rle_encode(text):
    if not text:
        return ''

    encoded = []
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1

    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)

    return ''.join(encoded)

def rle_decode(text):
    decoded = []
    i = 0
    while i < len(text):
        if text[i].isdigit():
            count = 0
            while i < len(text) and text[i].isdigit():
                count = count * 10 + int(text[i])
                i += 1
            char = text[i]
            decoded.append(char * count)
            i += 1
        else:
            decoded.append(text[i])
            i += 1

    return ''.join(decoded)

if __name__ == '__main__':
    sample_text = 'aaabbcdddd'
    encoded = rle_encode(sample_text)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)
    empty_encoded = rle_encode('')
    print(repr(empty_encoded))
    single_char_encoded = rle_encode('a')
    print(repr(single_char_encoded))
    mixed_encoded = rle_encode('aabbbccccc')
    print(mixed_encoded)
    mixed_decoded = rle_decode(mixed_encoded)
    print(mixed_decoded)