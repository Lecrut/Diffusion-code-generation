def rle_encode(data):
    if not data:
        return ""
    result = []
    index = 0
    while index < len(data):
        char = data[index]
        count = 1
        while index + 1 < len(data) and data[index + 1] == char:
            index += 1
            count += 1
        result.append(str(count) + char)
        index += 1
    return "".join(result)

if __name__ == '__main__':
    sample = "AABBCC"
    encoded = rle_encode(sample)
    print(encoded)