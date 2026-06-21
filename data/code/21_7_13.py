def run_length_encode(input_string):
    if not input_string:
        return []
    
    encoded_list = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded_list.append((current_char, count))
            current_char = input_string[i]
            count = 1
    
    encoded_list.append((current_char, count))
    return encoded_list

if __name__ == '__main__':
    result1 = run_length_encode("AAABBC")
    print(result1)
    result2 = run_length_encode("ABC")
    print(result2)
    result3 = run_length_encode("")
    print(result3)
    result4 = run_length_encode("AAAA")
    print(result4)
    
    assert result1 == [('A', 3), ('B', 2), ('C', 1)]
    assert result2 == [('A', 1), ('B', 1), ('C', 1)]
    assert result3 == []
    assert result4 == [('A', 4)]