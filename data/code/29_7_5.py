def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == "__main__":
    print(run_length_encode("AAABBBCCD"))
    print(run_length_encode("A"))
    print(run_length_encode("AABBCC"))
    print(run_length_encode("ABCDEFG"))
    print(run_length_encode("AAABBBCCC"))
    print(run_length_encode(""))
    print(run_length_encode("AAAAA"))
    print(run_length_encode("ABABAB"))
    print(run_length_encode("12345"))
    print(run_length_encode("!@#$%^&*()"))
    print(run_length_encode("   "))
    print(run_length_encode("a1b2c3"))
    print(run_length_encode("XyZ"))
    print(run_length_encode("Hello World"))
    print(run_length_encode("111222333"))
    print(run_length_encode("abcdefgabcdefg"))
    print(run_length_encode("AaBbCc"))
    print(run_length_encode("1a1a1a"))
    print(run_length_encode("!!!"))
    print(run_length_encode("a b c"))