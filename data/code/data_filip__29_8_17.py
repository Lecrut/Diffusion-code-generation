def encode_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccd"
    encoded_result = encode_string(sample_input)
    print(encoded_result)
    sample_input_2 = "aabbcc"
    print(encode_string(sample_input_2))
    sample_input_3 = "aaaaa"
    print(encode_string(sample_input_3))
    sample_input_4 = ""
    print(encode_string(sample_input_4))
    sample_input_5 = "z"
    print(encode_string(sample_input_5))