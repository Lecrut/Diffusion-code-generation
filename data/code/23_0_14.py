def run_length_encode(s: str) -> str:
    if not s:
        return s

    result = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1

    if count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)

    return "".join(result)

if __name__ == '__main__':
    samples = ["", "a", "aa", "aabbc", "abc", "aaaaaa"]
    for sample in samples:
        encoded = run_length_encode(sample)
        print(encoded)