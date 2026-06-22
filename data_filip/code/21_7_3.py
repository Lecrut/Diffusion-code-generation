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
    assert run_length_encoding("") == []
    assert run_length_encoding("a") == [("a", 1)]
    assert run_length_encoding("aaabbbcc") == [("a", 3), ("b", 3), ("c", 2)]
    assert run_length_encoding("112223333") == [("1", 2), ("2", 3), ("3", 4)]
    assert run_length_encoding("abc") == [("a", 1), ("b", 1), ("c", 1)]
    print(run_length_encoding("aaabbbcc"))
    print(run_length_encoding("112223333"))
    print(run_length_encoding("abc"))
    print(run_length_encoding(""))