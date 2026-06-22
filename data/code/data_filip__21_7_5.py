def run_length_encoding(s: str) -> list:
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    test_input_1 = "aaabbccccd"
    expected_1 = [('a', 3), ('b', 2), ('c', 4), ('d', 1)]
    assert run_length_encoding(test_input_1) == expected_1

    test_input_2 = "aaaa"
    expected_2 = [('a', 4)]
    assert run_length_encoding(test_input_2) == expected_2

    test_input_3 = ""
    expected_3 = []
    assert run_length_encoding(test_input_3) == expected_3

    test_input_4 = "a"
    expected_4 = [('a', 1)]
    assert run_length_encoding(test_input_4) == expected_4

    test_input_5 = "abbc"
    expected_5 = [('a', 1), ('b', 2), ('c', 1)]
    assert run_length_encoding(test_input_5) == expected_5

    print(run_length_encoding("aaabbccccd"))
    print(run_length_encoding("aaaa"))
    print(run_length_encoding(""))
    print(run_length_encoding("a"))
    print(run_length_encoding("abbc"))