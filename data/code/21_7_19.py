def run_length_encoding(s):
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    test_string_1 = "AAABBCDD"
    test_string_2 = "aAaA"
    test_string_3 = "1111222233"
    test_string_4 = ""
    test_string_5 = "a"
    
    assert run_length_encoding(test_string_1) == [('A', 3), ('B', 2), ('C', 1), ('D', 2)]
    assert run_length_encoding(test_string_2) == [('a', 1), ('A', 1), ('a', 1), ('A', 1)]
    assert run_length_encoding(test_string_3) == [('1', 4), ('2', 4), ('3', 2)]
    assert run_length_encoding(test_string_4) == []
    assert run_length_encoding(test_string_5) == [('a', 1)]
    
    print(run_length_encoding(test_string_1))
    print(run_length_encoding(test_string_2))
    print(run_length_encoding(test_string_3))
    print(run_length_encoding(test_string_4))
    print(run_length_encoding(test_string_5))