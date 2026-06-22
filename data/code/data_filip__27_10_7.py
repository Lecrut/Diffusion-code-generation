def run_length_encode(s):
    if not s:
        return ""

    encoded = []
    count = 1
    current_char = s[0]

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = s[i]
            count = 1

    encoded.append(current_char)
    encoded.append(str(count))

    return "".join(encoded)

if __name__ == "__main__":
    test_cases = [
        "",
        "a",
        "aaa",
        "aabbbcc",
        "abcdef",
        "aaabbbaaa"
    ]

    for case in test_cases:
        result = run_length_encode(case)
        print(result)