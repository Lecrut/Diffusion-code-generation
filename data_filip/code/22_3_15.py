def encode_rle(data):
    if not data:
        return ""
    encoded = []
    count = 1
    length = len(data)
    for i in range(length):
        if i + 1 < length and data[i] == data[i + 1]:
            count += 1
        else:
            encoded.append(str(count) + data[i])
            count = 1
    return "".join(encoded)

def decode_rle(data):
    if not data:
        return ""
    decoded = []
    count = 0
    for char in data:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            decoded.append(char * count)
            count = 0
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    encoded_result = encode_rle(sample_string)
    decoded_result = decode_rle(encoded_result)
    print(encoded_result)
    print(decoded_result)