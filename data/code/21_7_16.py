def run_length_encoding(s: str) -> list:
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
    test_string = "aaabbccccd"
    encoded = run_length_encoding(test_string)
    assert encoded == [('a', 3), ('b', 2), ('c', 4), ('d', 1)], "Test 1 failed"
    test_string_empty = ""
    encoded_empty = run_length_encoding(test_string_empty)
    assert encoded_empty == [], "Test 2 failed"
    test_string_single = "z"
    encoded_single = run_length_encoding(test_string_single)
    assert encoded_single == [('z', 1)], "Test 3 failed"
    test_string_multi = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
    encoded_multi = run_length_encoding(test_string_multi)
    assert encoded_multi == [('w', 50)], "Test 4 failed"
    print(encoded)
    print(encoded_empty)
    print(encoded_single)
    print(encoded_multi)