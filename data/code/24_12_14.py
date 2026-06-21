def rle_compress(data):
    if not data:
        return ""
    result = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(f"{count}{data[i-1]}")
            count = 1
    result.append(f"{count}{data[-1]}")
    return "".join(result)

if __name__ == '__main__':
    original_string = "AAAABBBCCDAA"
    compressed = rle_compress(original_string)
    print(original_string)
    print(compressed)