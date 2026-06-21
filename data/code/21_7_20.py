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
    sample_inputs = [
        "aaabbc",
        "abc",
        "aaaaa",
        "aabba",
        "",
        "z"
    ]
    for sample in sample_inputs:
        result = run_length_encoding(sample)
        print(f"Input: '{sample}' -> Output: {result}")
    
    assert run_length_encoding("aaabbc") == [('a', 3), ('b', 2), ('c', 1)]
    assert run_length_encoding("abc") == [('a', 1), ('b', 1), ('c', 1)]
    assert run_length_encoding("aaaaa") == [('a', 5)]
    assert run_length_encoding("aabba") == [('a', 2), ('b', 2), ('a', 1)]
    assert run_length_encoding("") == []
    assert run_length_encoding("z") == [('z', 1)]