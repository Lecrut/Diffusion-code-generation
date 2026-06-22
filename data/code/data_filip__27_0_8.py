def rle_encode(s: str) -> list:
    if not s:
        return []
    result = [(s[0], 1)]
    for c in s[1:]:
        if c == result[-1][0]:
            result[-1] = (result[-1][0], result[-1][1] + 1)
        else:
            result.append((c, 1))
    return result

if __name__ == '__main__':
    print(rle_encode("AAABBBCCDAA"))
    print(rle_encode(""))
    print(rle_encode("A"))
    print(rle_encode("ABC"))
    print(rle_encode("AAAA"))