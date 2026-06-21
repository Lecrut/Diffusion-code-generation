def run_length_encode(input_string):
    if not input_string:
        return []
    
    encoded_list = []
    current_char = input_string[0]
    current_count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            current_count += 1
        else:
            encoded_list.append((current_char, current_count))
            current_char = char
            current_count = 1
            
    encoded_list.append((current_char, current_count))
    
    return encoded_list

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = run_length_encode(sample_input)
    print(result)