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
    assert run_length_encode("") == []
    assert run_length_encode("a") == [('a', 1)]
    assert run_length_encode("aaa") == [('a', 3)]
    assert run_length_encode("aab") == [('a', 2), ('b', 1)]
    assert run_length_encode("aabbbcc") == [('a', 2), ('b', 3), ('c', 2)]
    assert run_length_encode("aaabbbccc") == [('a', 3), ('b', 3), ('c', 3)]
    assert run_length_encode("abcd") == [('a', 1), ('b', 1), ('c', 1), ('d', 1)]
    assert run_length_encode("aaabba") == [('a', 3), ('b', 2), ('a', 1)]
    result = run_length_encode("aabbbcc")
    print(result)