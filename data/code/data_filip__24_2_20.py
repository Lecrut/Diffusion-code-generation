def rle_encode(data):
    if not data:
        return ""
    result = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(str(count) + data[i - 1])
            count = 1
    result.append(str(count) + data[i])
    return "".join(result)

def rle_decode(data):
    if not data:
        return ""
    result = []
    count = 0
    for char in data:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            result.append(char * count)
            count = 0
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCD"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)
    print(original, encoded, decoded)