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
    result.append(str(count) + data[-1])
    return "".join(result)

if __name__ == '__main__':
    input_string = "AAABBBCCDAA"
    encoded = rle_encode(input_string)
    print(encoded)