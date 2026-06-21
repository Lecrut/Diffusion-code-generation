def compress_repeated_chars(s: str) -> str:
    if not s:
        return ""

    result = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = char
            count = 1

    result.append(current_char)
    if count > 1:
        result.append(str(count))

    return "".join(result)

if __name__ == '__main__':
    samples = [
        "",
        "a",
        "aaa",
        "aabbc",
        "aaabbcdddaaa",
        "abc",
        "aabbcccddd",
        "aaaaa",
        "aabbaaa",
        "python"
    ]
    for sample in samples:
        print(compress_repeated_chars(sample))