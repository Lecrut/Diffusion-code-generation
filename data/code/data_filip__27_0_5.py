def rle_encode(s: str) -> list:
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample1 = "AABCCCDEEEE"
    sample2 = "XYZ"
    sample3 = ""
    sample4 = "AAAAAAAAAA"
    print(rle_encode(sample1))
    print(rle_encode(sample2))
    print(rle_encode(sample3))
    print(rle_encode(sample4))