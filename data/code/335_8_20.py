def split_string(s: str, delimiter: str) -> list[str]:
    result = []
    start = 0
    for i in range(len(s)):
        if s[i] == delimiter:
            part = s[start:i]
            if part != '':
                result.append(part)
            start = i + 1
    last_part = s[start:]
    if last_part != '':
        result.append(last_part)
    return result
if __name__ == '__main__':
    sample_string = "apple,banana,cherry"
    delimiter = ","
    parts = split_string(sample_string, delimiter)
    print(parts)