def encode_rle(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(str(count) + text[i - 1])
            count = 1
    result.append(str(count) + text[-1])
    return "".join(result)

def decode_rle(encoded):
    if not encoded:
        return ""
    result = []
    count_str = ""
    for char in encoded:
        if char.isdigit():
            count_str += char
        else:
            count = int(count_str)
            result.append(char * count)
            count_str = ""
    return "".join(result)

if __name__ == '__main__':
    raw = "AAAAABBBCCD"
    compressed = encode_rle(raw)
    decompressed = decode_rle(compressed)
    print(f"{compressed} -> {decompressed}")