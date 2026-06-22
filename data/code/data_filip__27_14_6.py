def rle_encode(data):
    if not data:
        return ""
    encoded = []
    i = 0
    n = len(data)
    while i < n:
        count = 1
        while i + 1 < n and data[i] == data[i + 1]:
            i += 1
            count += 1
        encoded.append(f"{count}{data[i]}")
        i += 1
    return "".join(encoded)

if __name__ == '__main__':
    test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWW"
    result = rle_encode(test_string)
    print(result)