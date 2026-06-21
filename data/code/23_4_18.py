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
            result.append(current_char)
            result.append(str(count))
            current_char = s[i]
            count = 1
    result.append(current_char)
    result.append(str(count))
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbccccd"
    sample2 = "wwwwaaadexxxxxx"
    sample3 = "a"
    sample4 = "aabbccdd"
    sample5 = "aaabbbcccddd"
    sample6 = "112233"
    sample7 = "111222333"
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))
    print(run_length_encode(sample6))
    print(run_length_encode(sample7))