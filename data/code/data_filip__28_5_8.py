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
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def decode_rle(data):
    decoded = []
    count_str = ""
    for char in data:
        if char.isdigit():
            count_str += char
        else:
            count = int(count_str)
            decoded.append(char * count)
            count_str = ""
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDD"
    encoded_string = encode_rle(sample_input)
    decoded_string = decode_rle(encoded_string)
    print(sample_input == decoded_string)