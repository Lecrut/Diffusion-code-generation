def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample = "aaabbcdd"
    print(compress_string(sample))
    sample2 = "abcdef"
    print(compress_string(sample2))
    sample3 = ""
    print(compress_string(sample3))
    sample4 = "aaaa"
    print(compress_string(sample4))