def encode_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            result.append(f"{s[i]}{count}")
            count = 1
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "",
        "a",
        "aa",
        "aabbc",
        "aabbccdd",
        "aaaabbbbcccc",
        "1122334455"
    ]
    for case in test_cases:
        print(f"Input: '{case}' -> Output: '{encode_string(case)}'")