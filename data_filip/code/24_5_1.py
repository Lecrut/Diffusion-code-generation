def encode_rle(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{current_char}")
            else:
                encoded.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        encoded.append(f"{count}{current_char}")
    else:
        encoded.append(current_char)
    return "".join(encoded)

def decode_rle(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        if encoded[i].isdigit():
            count = int(encoded[i])
            i += 1
            while i < len(encoded) and encoded[i].isdigit():
                count = count * 10 + int(encoded[i])
                i += 1
            if i < len(encoded):
                char = encoded[i]
                decoded.append(char * count)
                i += 1
        else:
            decoded.append(encoded[i])
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_data = "AAABBBCCDAA"
    encoded = encode_rle(sample_data)
    print(encoded)
    decoded = decode_rle(encoded)
    print(decoded)
    empty_data = ""
    encoded_empty = encode_rle(empty_data)
    print(encoded_empty)
    decoded_empty = decode_rle(encoded_empty)
    print(decoded_empty)
    single_char = "A"
    encoded_single = encode_rle(single_char)
    print(encoded_single)
    decoded_single = decode_rle(encoded_single)
    print(decoded_single)
    multi_digit = "AAAAAAAAAA"
    encoded_multi = encode_rle(multi_digit)
    print(encoded_multi)
    decoded_multi = decode_rle(encoded_multi)
    print(decoded_multi)