def rle_encode(text):
    if not text:
        return
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            yield f"{count}{current_char}"
            current_char = char
            count = 1
    yield f"{count}{current_char}"

def rle_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        count = 0
        while i < len(encoded) and encoded[i].isdigit():
            count = count * 10 + int(encoded[i])
            i += 1
        char = encoded[i]
        i += 1
        decoded.append(char * count)
    return ''.join(decoded)

if __name__ == '__main__':
    sample = "AAAABBBCCDAA"
    encoded = list(rle_encode(sample))
    print(''.join(encoded))
    decoded = rle_decode(''.join(encoded))
    print(decoded)