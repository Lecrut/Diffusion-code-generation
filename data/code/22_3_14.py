def rle_encode(data):
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

def rle_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        if i < len(encoded):
            count = int(count_str) if count_str else 1
            char = encoded[i]
            i += 1
            decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    encoded_result = rle_encode(sample_string)
    decoded_result = rle_decode(encoded_result)
    print(encoded_result)
    print(decoded_result)