def encode_rle(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(text[i - 1])
            count = 1
    result.append(str(count))
    result.append(text[-1])
    return "".join(result)

def decode_rle(encoded):
    if not encoded:
        return ""
    result = []
    for i in range(0, len(encoded), 2):
        count = int(encoded[i])
        char = encoded[i + 1]
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    original = "AAAABBBCCDAA"
    encoded = encode_rle(original)
    print(encoded)
    decoded = decode_rle(encoded)
    print(decoded)