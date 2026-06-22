def rle_encode(data):
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + data[i])
        i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = 'AABBCC'
    encoded_value = rle_encode(sample_input)
    print(encoded_value)