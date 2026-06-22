def rle_encode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return "".join(result)

if __name__ == '__main__':
    input_string = 'AABBCC'
    encoded_result = rle_encode(input_string)
    print(encoded_result)