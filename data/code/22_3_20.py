def encode_rle(data):
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

def decode_rle(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        num_str = ""
        while i < len(data) and data[i].isdigit():
            num_str += data[i]
            i += 1
        if i < len(data):
            char = data[i]
            count = int(num_str)
            decoded.append(char * count)
        i += 1
    return "".join(decoded)

if __name__ == "__main__":
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = encode_rle(sample_string)
    decoded_result = decode_rle(encoded_result)
    print(encoded_result)
    print(decoded_result)