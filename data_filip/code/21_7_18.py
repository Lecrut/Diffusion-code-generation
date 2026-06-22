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
    test_cases = [
        ("", []),
    ("AAABBC", [('A', 3), ('B', 2), ('C', 1)]),
    ("XYZ", [('X', 1), ('Y', 1), ('Z', 1)]),
    ("AAAAA", [('A', 5)]),
    ("A", [('A', 1)]),
    ("ABAB", [('A', 1), ('B', 1), ('A', 1), ('B', 1)]),
    ]
    
    for input_str, expected in test_cases:
        result = run_length_encode(input_str)
        assert result == expected, f"Failed on {input_str}: expected {expected}, got {result}"
        print(result)