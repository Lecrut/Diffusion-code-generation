def rle_encode(s):
    if not s:
        return ''
    encoded = []
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + s[i - 1])
            count = 1
    return ''.join(encoded)

if __name__ == '__main__':
    sample = 'AAAAABBBB'
    print(rle_encode(sample))