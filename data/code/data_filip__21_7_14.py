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
    sample_input = "AAABBBCCDAA"
    result = run_length_encode(sample_input)
    print(result)
    assert result == [('A', 3), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]
    assert run_length_encode("") == []
    assert run_length_encode("A") == [('A', 1)]
    assert run_length_encode("ABC") == [('A', 1), ('B', 1), ('C', 1)]
    assert run_length_encode("AAAA") == [('A', 4)]
    print("All assertions passed.")