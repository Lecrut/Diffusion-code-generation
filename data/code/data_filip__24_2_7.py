def rle_encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            count = 1
            current_char = data[i]
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def rle_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        num_str = []
        while i < len(encoded) and encoded[i].isdigit():
            num_str.append(encoded[i])
            i += 1
        count = int("".join(num_str))
        char = encoded[i]
        i += 1
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAAAABBBCCDAA"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)
    print(original)
    print(encoded)
    print(decoded)
    print(original == decoded)

    test2 = "abc"
    encoded2 = rle_encode(test2)
    decoded2 = rle_decode(encoded2)
    print(test2)
    print(encoded2)
    print(decoded2)
    print(test2 == decoded2)