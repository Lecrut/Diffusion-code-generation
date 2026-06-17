def split_string(s: str, delimiter: str) -> list[str]:
    parts = []
    start = 0
    for i in range(len(s)):
        if s[i] == delimiter:
            end = i + len(delimiter)
            parts.append(s[start:end])
            start = end
    parts.append(s[start:])
    return parts
if __name__ == '__main__':
    test_string = "apple,banana,cherry"
    result = split_string(test_string, ",")
    print(result)