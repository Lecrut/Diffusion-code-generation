def rle_decompress(compressed):
    if not compressed:
        return ""
    original = []
    i = 0
    while i < len(compressed):
        char = compressed[i]
        if char.isdigit():
            start = i
            while i < len(compressed) and compressed[i].isdigit():
                i += 1
            count = int(compressed[start:i])
            if i < len(compressed):
                original.append(compressed[i] * count)
                i += 1
            else:
                raise ValueError("Invalid RLE string: digit sequence not followed by a character")
        else:
            original.append(char)
            i += 1
    return "".join(original)

if __name__ == '__main__':
    compressed = "A5B3C2"
    result = rle_decompress(compressed)
    print(result)