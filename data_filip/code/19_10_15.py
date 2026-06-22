def compress_rle(data):
    if not data:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(str(count))
            compressed.append(data[i - 1])
            count = 1
    compressed.append(str(count))
    compressed.append(data[-1])
    return "".join(compressed)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWB"
    result = compress_rle(sample_string)
    print(result)