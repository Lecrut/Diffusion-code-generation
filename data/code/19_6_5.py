def rle_encode_case_insensitive(s):
    if not s:
        return ""
    s_lower = s.lower()
    result = []
    current_char = s_lower[0]
    count = 1
    for char in s_lower[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    samples = [
        "AAbbcccDD",
        "Hello World!",
        "aAaA",
        "ZZZZz",
        "",
        "abcABC"
    ]
    for sample in samples:
        encoded = rle_encode_case_insensitive(sample)
        print(f"Input: '{sample}' -> Output: '{encoded}'")