def run_length_encode(s):
    if not s:
        return ""
    if len(s) == 1:
        return s[0] + '1'

    encoded = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = s[i]
            count = 1

    encoded.append(current_char)
    encoded.append(str(count))

    return ''.join(encoded)

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aaa"))
    print(run_length_encode("aab"))
    print(run_length_encode("aabbcc"))
    print(run_length_encode("abc"))
    print(run_length_encode("aaabbaac"))