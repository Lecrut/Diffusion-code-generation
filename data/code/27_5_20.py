def rle_encode(s):
    if not s:
        return ''
    result = []
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count) + s[i - 1])
            count = 1
    return ''.join(result)

if __name__ == '__main__':
    print(rle_encode('AAAAABBBB'))