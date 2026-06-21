def run_length_encode(input_string):
    if not input_string:
        return []
    
    result = []
    current_char = input_string[0]
    current_count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            current_count += 1
        else:
            result.append((current_char, current_count))
            current_char = char
            current_count = 1
            
    result.append((current_char, current_count))
    return result

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)