def run_length_encode(s):
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
    sample1 = "aaabbc"
    result1 = run_length_encode(sample1)
    print(result1)
    assert result1 == [('a', 3), ('b', 2), ('c', 1)]

    sample2 = "a"
    result2 = run_length_encode(sample2)
    print(result2)
    assert result2 == [('a', 1)]

    sample3 = ""
    result3 = run_length_encode(sample3)
    print(result3)
    assert result3 == []

    sample4 = "aabbaaaccc"
    result4 = run_length_encode(sample4)
    print(result4)
    assert result4 == [('a', 2), ('b', 2), ('a', 3), ('c', 3)]

    sample5 = "xyz"
    result5 = run_length_encode(sample5)
    print(result5)
    assert result5 == [('x', 1), ('y', 1), ('z', 1)]