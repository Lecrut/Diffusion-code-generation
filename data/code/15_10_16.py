def compress_string(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
    result.append(current_char + str(count))
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == "__main__":
    sample_strings = [
        "aabcccccaaa",
        "abcdef",
        "aaabbbccc",
        "aabbcc",
        "mississippi",
        "",
        "a"
    ]
    for s in sample_strings:
        print(compress_string(s))