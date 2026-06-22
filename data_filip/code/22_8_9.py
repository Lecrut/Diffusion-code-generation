def rle_compress(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbcdddd"
    compressed = rle_compress(sample_string)
    print(compressed)