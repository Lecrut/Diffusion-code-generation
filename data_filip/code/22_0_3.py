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
            if count > 1:
                result.append(str(count))
            current_char = s[i]
            count = 1

    result.append(current_char)
    if count > 1:
        result.append(str(count))

    return "".join(result)

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    print(run_length_encode(sample1))
    sample2 = "abcdef"
    print(run_length_encode(sample2))
    sample3 = ""
    print(run_length_encode(sample3))
    sample4 = "a"
    print(run_length_encode(sample4))
    sample5 = "aa"
    print(run_length_encode(sample5))