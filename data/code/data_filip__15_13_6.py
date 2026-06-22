def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = s[i]
            count = 1
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccddeeef"
    print(compress_string(sample_input))
    sample_input_2 = "abc"
    print(compress_string(sample_input_2))
    sample_input_3 = "a"
    print(compress_string(sample_input_3))