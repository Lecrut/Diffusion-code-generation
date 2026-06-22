def run_length_encode(input_str):
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    if len(input_str) == 0:
        return []
    
    char_counts = {}
    run_list = []
    current_char = input_str[0]
    current_count = 0
    
    for char in input_str:
        if char == current_char:
            current_count += 1
            char_counts[char] = current_count
        else:
            run_list.append((current_char, char_counts[current_char]))
            char_counts = {}
            current_char = char
            char_counts[current_char] = 1
            current_count = 1
            
    run_list.append((current_char, char_counts[current_char]))
    return run_list

if __name__ == '__main__':
    sample_data = 'aabbaaccc'
    result = run_length_encode(sample_data)
    print(result)