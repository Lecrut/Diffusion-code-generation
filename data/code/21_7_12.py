def run_length_encode(input_str):
    if not input_str:
        return []
    
    result = []
    current_char = input_str[0]
    count = 1
    
    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = input_str[i]
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    test_cases = [
        ("AAABBBCCCC", [('A', 3), ('B', 3), ('C', 4)]),
        ("ABC", [('A', 1), ('B', 1), ('C', 1)]),
        ("", []),
        ("A", [('A', 1)]),
        ("AAAA", [('A', 4)]),
    ]
    
    for input_str, expected in test_cases:
        result = run_length_encode(input_str)
        assert result == expected, f"Failed for {input_str}: expected {expected}, got {result}"
    
    print(run_length_encode("AAABBBCCCC"))