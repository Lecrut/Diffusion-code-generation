def rle_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = data[i]
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def rle_decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        count = ""
        while i < len(data) and data[i].isdigit():
            count += data[i]
            i += 1
        if i < len(data):
            decoded.append(data[i] * int(count))
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = rle_encode(sample_string)
    decoded_result = rle_decode(encoded_result)
    print(encoded_result)
    print(decoded_result)