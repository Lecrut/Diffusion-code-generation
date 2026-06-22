def rle_compress(data):
    if not data:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(f"{data[i - 1]}{count}")
            count = 1
    compressed.append(f"{data[-1]}{count}")
    return "".join(compressed)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = rle_compress(sample_string)
    print(result)