def encode_repeated_elements(s):
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
    sample_strings = ["aabcccccaaa", "abcdef", "aaaaaa", "aaabbcccc", "a"]
    for sample in sample_strings:
        print(encode_repeated_elements(sample))