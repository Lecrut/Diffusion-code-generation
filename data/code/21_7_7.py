def run_length_encoding(s):
    if not s:
        return []
    result = []
    count = 1
    current_char = s[0]
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
    assert run_length_encoding("aaabbbcc") == [('a', 3), ('b', 3), ('c', 2)]
    assert run_length_encoding("abcdef") == [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
    assert run_length_encoding("aabbccddeeff") == [('a', 2), ('b', 2), ('c', 2), ('d', 2), ('e', 2), ('f', 2)]
    assert run_length_encoding("zzzzyyyxxx") == [('z', 4), ('y', 3), ('x', 3)]
    assert run_length_encoding("") == []
    assert run_length_encoding("a") == [('a', 1)]
    print(run_length_encoding("aaabbbcc"))
    print(run_length_encoding("abcdef"))
    print(run_length_encoding("aabbccddeeff"))
    print(run_length_encoding("zzzzyyyxxx"))
    print(run_length_encoding(""))
    print(run_length_encoding("a"))