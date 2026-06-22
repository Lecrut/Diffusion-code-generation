def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = s[i]
            count = 1
    encoded.append(current_char + str(count))
    return "".join(encoded)

if __name__ == '__main__':
    test_string_1 = "aaabbccccccddd"
    test_string_2 = "a"
    test_string_3 = "aabbcc"
    test_string_4 = "1122233334"
    result_1 = run_length_encode(test_string_1)
    result_2 = run_length_encode(test_string_2)
    result_3 = run_length_encode(test_string_3)
    result_4 = run_length_encode(test_string_4)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)