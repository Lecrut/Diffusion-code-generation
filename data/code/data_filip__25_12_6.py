def rle_encode(data: str) -> str:
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def rle_decode(data: str) -> str:
    if not data:
        return ""
    decoded = []
    count_str = ""
    i = 0
    while i < len(data):
        if data[i].isdigit():
            count_str += data[i]
        else:
            count = int(count_str)
            decoded.append(data[i] * count)
            count_str = ""
        i += 1
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAABBBCCCCCDDEEEE"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)
    single = "X"
    enc_single = rle_encode(single)
    dec_single = rle_decode(enc_single)
    print(enc_single)
    print(dec_single)
    alternating = "ABABAB"
    enc_alt = rle_encode(alternating)
    dec_alt = rle_decode(enc_alt)
    print(enc_alt)
    print(dec_alt)
    empty = ""
    enc_empty = rle_encode(empty)
    dec_empty = rle_decode(enc_empty)
    print(enc_empty)
    print(dec_empty)