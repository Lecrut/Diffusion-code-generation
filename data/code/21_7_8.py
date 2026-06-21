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
    test_input_1 = "aaabbcccc"
    test_input_2 = "a"
    test_input_3 = ""
    test_input_4 = "aabbc"
    
    result_1 = run_length_encoding(test_input_1)
    assert result_1 == [('a', 3), ('b', 2), ('c', 4)]
    print(result_1)
    
    result_2 = run_length_encoding(test_input_2)
    assert result_2 == [('a', 1)]
    print(result_2)
    
    result_3 = run_length_encoding(test_input_3)
    assert result_3 == []
    print(result_3)
    
    result_4 = run_length_encoding(test_input_4)
    assert result_4 == [('a', 2), ('b', 2), ('c', 1)]
    print(result_4)