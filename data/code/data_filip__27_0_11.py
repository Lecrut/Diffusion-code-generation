def rle_encode(s: str) -> list:
    if not s:
        return []
    result = [(s[0], 1)]
    for char in s[1:]:
        if char == result[-1][0]:
            result[-1] = (result[-1][0], result[-1][1] + 1)
        else:
            result.append((char, 1))
    return result

if __name__ == '__main__':
    sample = "AAABBBCCDAA"
    print(rle_encode(sample))
    print(rle_encode(""))
    print(rle_encode("A"))
    print(rle_encode("ABCDEFG"))
    print(rle_encode("AAABBBCCC"))