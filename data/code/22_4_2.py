def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aaabbbcc"))
    print(run_length_encode("aabbbcccc"))
    print(run_length_encode("abc"))
    print(run_length_encode("aaaa"))
    print(run_length_encode("aabbcc"))
    print(run_length_encode("w3e"))