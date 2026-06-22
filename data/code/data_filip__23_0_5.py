def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    compressed = "".join(result)
    if len(compressed) < len(s):
        return compressed
    return s

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aaa"))
    print(run_length_encode("aabbbcccc"))
    print(run_length_encode("abc"))
    print(run_length_encode("aaabbbccc"))