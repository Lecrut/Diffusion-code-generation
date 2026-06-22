def encode_rle(data):
    if not data:
        return []
    result = []
    count = 1
    current_char = data[0]
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

def decode_rle(encoded_data):
    if not encoded_data:
        return ""
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbbcccaabb"
    encoded = encode_rle(sample_text)
    decoded = decode_rle(encoded)
    print(
        (encoded, decoded)
    )