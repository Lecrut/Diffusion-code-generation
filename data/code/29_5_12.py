def encode_rle(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
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
    sample_strings = ["", "a", "aa", "aabbbcccc", "aabbbaa"]
    for s in sample_strings:
        print(encode_rle(s))