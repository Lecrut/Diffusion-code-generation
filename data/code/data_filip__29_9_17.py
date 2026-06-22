def encode_repeated_elements(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{s[i - 1]}")
            else:
                result.append(s[i - 1])
            count = 1
    if count > 1:
        result.append(f"{count}{s[-1]}")
    else:
        result.append(s[-1])
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbccccd"
    encoded_string = encode_repeated_elements(sample_string)
    print(encoded_string)
    sample_string_2 = "hello"
    encoded_string_2 = encode_repeated_elements(sample_string_2)
    print(encoded_string_2)
    sample_string_3 = "a"
    encoded_string_3 = encode_repeated_elements(sample_string_3)
    print(encoded_string_3)
    sample_string_4 = ""
    encoded_string_4 = encode_repeated_elements(sample_string_4)
    print(encoded_string_4)