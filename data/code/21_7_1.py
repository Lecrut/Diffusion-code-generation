def run_length_encode(input_string):
    if not input_string:
        return []

    result = []
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    assert run_length_encode('') == []
    assert run_length_encode('a') == [('a', 1)]
    assert run_length_encode('aaabbcc') == [('a', 3), ('b', 2), ('c', 2)]
    assert run_length_encode('abcdef') == [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
    assert run_length_encode('aaabbbccc') == [('a', 3), ('b', 3), ('c', 3)]
    print(run_length_encode('aaabbbccc'))
    print(run_length_encode('abcdef'))
    print(run_length_encode(''))