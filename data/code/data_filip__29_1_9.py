def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{current_char}{count}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.append(f"{current_char}{count}")
    else:
        result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcdd"
    print(compress_string(sample_input))
    sample_input2 = "abcd"
    print(compress_string(sample_input2))
    sample_input3 = "aabbcc"
    print(compress_string(sample_input3))
    sample_input4 = ""
    print(compress_string(sample_input4))
    sample_input5 = "aaaa"
    print(compress_string(sample_input5))