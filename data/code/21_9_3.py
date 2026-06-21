def run_length_encoding(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(s[i - 1])
            count = 1
    result.append(str(count))
    result.append(s[-1])
    return "".join(result)

if __name__ == '__main__':
    test_string = "aaabbcccc"
    encoded = run_length_encoding(test_string)
    print(encoded)
    empty_string = ""
    encoded_empty = run_length_encoding(empty_string)
    print(encoded_empty)
    single_char = "z"
    encoded_single = run_length_encoding(single_char)
    print(encoded_single)