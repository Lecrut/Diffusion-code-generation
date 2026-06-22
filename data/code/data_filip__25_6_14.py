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

def run_length_decode(s):
    result = []
    i = 0
    while i < len(s):
        count = 0
        while i < len(s) and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1
        if i < len(s):
            char = s[i]
            i += 1
            result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("a"))
    print(run_length_encode("aaa"))
    print(run_length_encode("aabbc"))
    print(run_length_encode("aabbcc"))
    print(run_length_encode("aaabbbccc"))
    print(run_length_decode("3a2b1c"))
    print(run_length_decode("1a"))
    print(run_length_decode(""))