def encode_repeating_characters(s):
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
            result.append(str(count))
            current_char = char
            count = 1
    result.append(current_char)
    result.append(str(count))
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "aabccc"
    print(encode_repeating_characters(sample1))
    sample2 = "aaaaabbbcc"
    print(encode_repeating_characters(sample2))
    sample3 = "abcdef"
    print(encode_repeating_characters(sample3))
    sample4 = ""
    print(encode_repeating_characters(sample4))