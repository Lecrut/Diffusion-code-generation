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
    test_cases = [
        ("aabbcc", [('a', 2), ('b', 2), ('c', 2)]),
        ("aaaabbb", [('a', 4), ('b', 3)]),
        ("", []),
        ("single", [('s', 1), ('i', 1), ('n', 1), ('g', 1), ('l', 1), ('e', 1)]),
        ("1122333", [('1', 2), ('2', 2), ('3', 3)]),
    ]
    for input_str, expected in test_cases:
        result = run_length_encode(input_str)
        assert result == expected, f"Failed for {input_str}: got {result}, expected {expected}"
    print(run_length_encode("aabbcc"))
    print(run_length_encode("aaaabbb"))
    print(run_length_encode(""))
    print(run_length_encode("single"))
    print(run_length_encode("1122333"))