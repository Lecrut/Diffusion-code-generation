def run_length_encoding(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{count}{s[i - 1]}")
            count = 1
    result.append(f"{count}{s[-1]}")
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbcdddd"
    sample2 = "a"
    sample3 = ""
    print(run_length_encoding(sample1))
    print(run_length_encoding(sample2))
    print(run_length_encoding(sample3))