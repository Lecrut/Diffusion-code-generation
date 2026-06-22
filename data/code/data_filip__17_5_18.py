def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_parts = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded_parts.append(f"{count}{current_char}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "AAABBBCCCDDDEEEFFGG"
    result = run_length_encode(sample_input)
    print(result)
    
    sample_input2 = "ABCDEF"
    result2 = run_length_encode(sample_input2)
    print(result2)
    
    sample_input3 = ""
    result3 = run_length_encode(sample_input3)
    print(result3)
    
    sample_input4 = "AAAAAAAAAA"
    result4 = run_length_encode(sample_input4)
    print(result4)