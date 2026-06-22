def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            result.append(str(count))
            count = 1
    result.append(s[-1])
    result.append(str(count))
    return "".join(result)

if __name__ == '__main__':
    sample = 'aaaaabbcccd'
    print(compress_string(sample))