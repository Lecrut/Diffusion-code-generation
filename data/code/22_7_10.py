def decode_rle(s):
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        i += 1
        if i < n and s[i].isdigit():
            j = i
            while j < n and s[j].isdigit():
                j += 1
            count = int(s[i:j])
            i = j
            result.append(c * count)
        else:
            result.append(c)
    return "".join(result)

if __name__ == '__main__':
    compressed = "a3b2c1d"
    decoded = decode_rle(compressed)
    print(decoded)