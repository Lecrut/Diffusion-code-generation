def run_length_encode(input_string):
    if not input_string:
        return ""
    
    if len(input_string) == 1:
        return input_string
    
    encoded = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = run_length_encode(sample_input)
    print(result)
    
    empty_input = ""
    empty_result = run_length_encode(empty_input)
    print(empty_result)
    
    no_repeat_input = "abc"
    no_repeat_result = run_length_encode(no_repeat_input)
    print(no_repeat_result)
    
    single_char_input = "z"
    single_char_result = run_length_encode(single_char_input)
    print(single_char_result)