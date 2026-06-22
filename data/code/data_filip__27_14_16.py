def rle_encode(data):
    if not data:
        return ""
    encoded = []
    prev = data[0]
    count = 1
    for char in data[1:]:
        if char == prev:
            count += 1
        else:
            encoded.append(f"{prev}{count}")
            prev = char
            count = 1
    encoded.append(f"{prev}{count}")
    return "".join(encoded)

if __name__ == "__main__":
    test_string = "AAAAAAABBBCCDAABBB"
    result = rle_encode(test_string)
    print(result)