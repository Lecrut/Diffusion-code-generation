def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCD",
        "ABCDE",
        "AABBCC",
        "",
        "AAAAA",
        "ABABAB"
    ]
    for s in sample_strings:
        print(run_length_encode(s))