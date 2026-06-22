def rle_encode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        result.append(str(count) + s[i])
        i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = 'AABBCC'
    encoded_result = rle_encode(sample_input)
    print(encoded_result)