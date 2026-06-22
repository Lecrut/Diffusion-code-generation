def rle_encode(s):
    if not s:
        return ""
    encoded = []
    i = 0
    n = len(s)
    while i < n:
        count = 1
        while i + count < n and s[i + count] == s[i]:
            count += 1
        encoded.append(str(count) + s[i])
        i += count
    return "".join(encoded)

if __name__ == '__main__':
    result = rle_encode('AABBCC')
    print(result)