def rle_encode(text: str) -> str:
    if not text:
        return text

    result = []
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1

    if count > 1:
        result.append(str(count))
    result.append(current_char)

    encoded = "".join(result)
    if len(encoded) >= len(text):
        return text
    return encoded

if __name__ == '__main__':
    sample1 = "aaabbc"
    print(rle_encode(sample1))

    sample2 = "abc"
    print(rle_encode(sample2))

    sample3 = ""
    print(rle_encode(sample3))

    sample4 = "a"
    print(rle_encode(sample4))

    sample5 = "aaaaa"
    print(rle_encode(sample5))