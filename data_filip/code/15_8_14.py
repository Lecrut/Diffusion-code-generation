def compress_string(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = s[i]
            count = 1
    result.append(current_char)
    result.append(str(count))
    return "".join(result)

if __name__ == '__main__':
    print(compress_string("hello"))