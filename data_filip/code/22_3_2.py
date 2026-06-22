def encode(text):
    if not text:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{text[i - 1]}")
            count = 1
    encoded.append(f"{count}{text[-1]}")
    return "".join(encoded)

def decode(rle_string):
    if not rle_string:
        return ""
    decoded = []
    i = 0
    while i < len(rle_string):
        count = ""
        while i < len(rle_string) and rle_string[i].isdigit():
            count += rle_string[i]
            i += 1
        char = rle_string[i]
        decoded.append(char * int(count))
        i += 1
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAABBBCCD"
    encoded_text = encode(original)
    print(encoded_text)
    decoded_text = decode(encoded_text)
    print(decoded_text)