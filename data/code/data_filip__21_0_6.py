def run_length_encode(s):
    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1

    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_strings = [
        "aaabbc",
        "abcdef",
        "aaaaa",
        "",
        "aabbcc",
        "xyyzww"
    ]

    for test_str in sample_strings:
        encoded = run_length_encode(test_str)
        print(f"Input: '{test_str}' -> Output: {encoded}")