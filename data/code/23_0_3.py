def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(f"{s[i - 1]}{count}")
            else:
                result.append(s[i - 1])
            count = 1
    if count > 1:
        result.append(f"{s[-1]}{count}")
    else:
        result.append(s[-1])
    return "".join(result)

if __name__ == "__main__":
    sample1 = "aaabbbcccc"
    sample2 = "abcdef"
    sample3 = ""
    sample4 = "a"
    sample5 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))