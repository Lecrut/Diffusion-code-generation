def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = s[i]
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    print(run_length_encode("AAABBBCCD"))
    print(run_length_encode("ABC"))
    print(run_length_encode("AAAA"))
    print(run_length_encode(""))
    print(run_length_encode("A"))
    print(run_length_encode("aabbbcccc"))
    print(run_length_encode("1122333"))
    print(run_length_encode("!@#$%^&*()"))
    print(run_length_encode("a1b2c3"))