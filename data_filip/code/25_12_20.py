def encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            count = 1
            current_char = data[i]
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def decode(data):
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
            decoded.append(char * int(num_str))
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    test_string = "AAABBBCCCCDDDDDDD"
    encoded_result = encode(test_string)
    decoded_result = decode(encoded_result)
    print(encoded_result)
    print(decoded_result)