def run_length_encode(s):
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
    sample1 = "aaabbc"
    result1 = run_length_encode(sample1)
    print(result1)
    assert result1 == [('a', 3), ('b', 2), ('c', 1)]

    sample2 = "abc"
    result2 = run_length_encode(sample2)
    print(result2)
    assert result2 == [('a', 1), ('b', 1), ('c', 1)]

    sample3 = "aaaaa"
    result3 = run_length_encode(sample3)
    print(result3)
    assert result3 == [('a', 5)]

    sample4 = ""
    result4 = run_length_encode(sample4)
    print(result4)
    assert result4 == []

    sample5 = "aabbccddeeff"
    result5 = run_length_encode(sample5)
    print(result5)
    assert result5 == [('a', 2), ('b', 2), ('c', 2), ('d', 2), ('e', 2), ('f', 2)]

    sample6 = "mississippi"
    result6 = run_length_encode(sample6)
    print(result6)
    assert result6 == [('m', 1), ('i', 1), ('s', 2), ('i', 1), ('s', 2), ('i', 1), ('p', 2), ('i', 1)]