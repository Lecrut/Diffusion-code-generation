def encode_run_length(s: str) -> str:
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
    test_cases = ["", "a", "aa", "aabbbc", "wwwwaaadexxxxxx", "112233"]
    for case in test_cases:
        print(f"Input: '{case}' -> Output: '{encode_run_length(case)}'")