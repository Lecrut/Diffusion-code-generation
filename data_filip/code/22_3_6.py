def encode(data):
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

def decode(encoded_data):
    if not encoded_data:
        return ""
    decoded = []
    i = 0
    while i < len(encoded_data):
        if encoded_data[i].isdigit():
            num_str = ""
            while i < len(encoded_data) and encoded_data[i].isdigit():
                num_str += encoded_data[i]
                i += 1
            count = int(num_str)
            char = encoded_data[i]
            i += 1
            decoded.append(char * count)
        else:
            decoded.append(encoded_data[i])
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAAABBBCCDEEEE"
    encoded_str = encode(original)
    print(encoded_str)
    decoded_str = decode(encoded_str)
    print(decoded_str)