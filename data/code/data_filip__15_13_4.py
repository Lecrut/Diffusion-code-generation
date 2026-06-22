def compress_string(s):
    if not s:
        return s
    result = []
    count = 1
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            if count > 1:
                result.append(str(count))
            count = 1
    result.append(s[n - 1])
    if count > 1:
        result.append(str(count))
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "aaabbcdddddeee"
    output = compress_string(sample_input)
    print(output)