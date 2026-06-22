def encode_rle(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = text[i]
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

def decode_rle(encoded):
    if not encoded:
        return ""
    result = []
    i = 0
    while i < len(encoded):
        if i + 1 < len(encoded) and encoded[i].isdigit() and encoded[i+1].isdigit():
            count = int(encoded[i:i+2])
            char = encoded[i+2]
            result.append(char * count)
            i += 3
        else:
            count = int(encoded[i])
            char = encoded[i+1]
            result.append(char * count)
            i += 2
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAABBC"
    encoded = encode_rle(sample_text)
    decoded = decode_rle(encoded)
    print(decoded == sample_text)