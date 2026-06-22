def run_length_encode(data):
    if not data:
        return {}
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    counts = {}
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            counts[current_char] = counts.get(current_char, 0) + count
            current_char = data[i]
            count = 1
    counts[current_char] = counts.get(current_char, 0) + count
    return counts

if __name__ == '__main__':
    test_string = "aaabbbaaccccc"
    result = run_length_encode(test_string)
    print(result)
    
    empty_string = ""
    empty_result = run_length_encode(empty_string)
    print(empty_result)
    
    single_char = "z"
    single_result = run_length_encode(single_char)
    print(single_result)
    
    mixed_string = "a1b2c3"
    mixed_result = run_length_encode(mixed_string)
    print(mixed_result)