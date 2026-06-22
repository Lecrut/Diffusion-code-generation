def run_length_encode(s):
    if not s:
        return {}
    result = {}
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = s[i]
            count = 1
    result[current_char] = count
    return result

if __name__ == '__main__':
    test_string = "aaabbccccdd"
    encoded_result = run_length_encode(test_string)
    print(encoded_result)
    test_string_empty = ""
    encoded_empty = run_length_encode(test_string_empty)
    print(encoded_empty)
    test_string_single = "a"
    encoded_single = run_length_encode(test_string_single)
    print(encoded_single)