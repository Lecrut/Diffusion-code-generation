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
            result.append(current_char + str(count))
            current_char = s[i]
            count = 1
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccaaa"
    print(compress_string(sample_input))
    sample_input2 = "a"
    print(compress_string(sample_input2))
    sample_input3 = ""
    print(compress_string(sample_input3))
    sample_input4 = "abcd"
    print(compress_string(sample_input4))