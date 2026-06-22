def run_length_encoding(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    sample2 = "aabbcc"
    sample3 = ""
    sample4 = "aaaa"
    print(run_length_encoding(sample1))
    print(run_length_encoding(sample2))
    print(run_length_encoding(sample3))
    print(run_length_encoding(sample4))