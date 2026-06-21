def rle_encode(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        count = 1
        while i + 1 < len(s) and s[i + 1] == char:
            count += 1
            i += 1
        if count == 1:
            result.append(char)
        else:
            result.append(str(count))
            result.append(char)
        i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccddddeeeefff"
    encoded_result = rle_encode(sample_input)
    print(encoded_result)