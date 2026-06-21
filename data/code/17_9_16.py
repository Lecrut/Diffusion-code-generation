def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_parts = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = input_string[i]
            count = 1
    
    encoded_parts.append(f"{current_char}{count}")
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "AAABBC"
    result = run_length_encode(sample_input)
    print(result)
    
    empty_input = ""
    empty_result = run_length_encode(empty_input)
    print(empty_result)
    
    single_input = "Z"
    single_result = run_length_encode(single_input)
    print(single_result)
    
    mixed_input = "11122233"
    mixed_result = run_length_encode(mixed_input)
    print(mixed_result)