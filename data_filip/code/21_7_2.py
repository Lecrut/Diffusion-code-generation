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
    result1 = run_length_encode("aabcccccaaa")
    assert result1 == [('a', 2), ('b', 1), ('c', 5), ('a', 3)]

    result2 = run_length_encode("")
    assert result2 == []

    result3 = run_length_encode("abcdef")
    assert result3 == [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]

    result4 = run_length_encode("aaaaa")
    assert result4 == [('a', 5)]

    result5 = run_length_encode("abAB")
    assert result5 == [('a', 1), ('b', 1), ('A', 1), ('B', 1)]

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)