def encode_rle(data):
    if not data:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + data[i - 1])
            count = 1
    encoded.append(str(count) + data[-1])
    return "".join(encoded)

def decode_rle(encoded_data):
    if not encoded_data:
        return ""
    decoded = []
    i = 0
    while i < len(encoded_data):
        count_str = ""
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count_str += encoded_data[i]
            i += 1
        if i < len(encoded_data):
            char = encoded_data[i]
            count = int(count_str)
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    encoded_result = encode_rle(sample_string)
    decoded_result = decode_rle(encoded_result)
    print(encoded_result)
    print(decoded_result)