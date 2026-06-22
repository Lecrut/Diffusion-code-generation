def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    length = len(s)
    for i in range(1, length):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[length - 1] + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    compressed = compress_string(sample_input)
    print(compressed)