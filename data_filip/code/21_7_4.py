def run_length_encode(input_string: str) -> list:
    if not input_string:
        return []
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    assert run_length_encode("aaabbca") == [('a', 3), ('b', 2), ('c', 1), ('a', 1)]
    assert run_length_encode("abc") == [('a', 1), ('b', 1), ('c', 1)]
    assert run_length_encode("aaa") == [('a', 3)]
    assert run_length_encode("") == []
    
    encoded = run_length_encode("aabcccccaaa")
    print(encoded)