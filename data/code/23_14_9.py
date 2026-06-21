def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    test_string = "aaabbcdddd"
    encoded_value = run_length_encode(test_string)
    print(encoded_value)
    empty_string = ""
    encoded_empty = run_length_encode(empty_string)
    print(encoded_empty)
    single_char = "a"
    encoded_single = run_length_encode(single_char)
    print(encoded_single)