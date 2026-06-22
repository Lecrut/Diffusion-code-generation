def run_length_encode(input_string):
    if not input_string:
        return []
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = input_string[i]
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    assert run_length_encode("") == []
    assert run_length_encode("A") == [("A", 1)]
    assert run_length_encode("AAABBC") == [("A", 3), ("B", 2), ("C", 1)]
    assert run_length_encode("XYZ") == [("X", 1), ("Y", 1), ("Z", 1)]
    
    encoded_value = run_length_encode("AAABBC")
    print(encoded_value)