def rle_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(f"{count}{text[i - 1]}")
            count = 1
    result.append(f"{count}{text[-1]}")
    return "".join(result)

def rle_decode(encoded):
    if not encoded:
        return ""
    result = []
    i = 0
    while i < len(encoded):
        count = ""
        while i < len(encoded) and encoded[i].isdigit():
            count += encoded[i]
            i += 1
        if i < len(encoded):
            char = encoded[i]
            i += 1
            result.append(char * int(count))
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCD"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)
    print(original == decoded)
    print(encoded)
    print(decoded)