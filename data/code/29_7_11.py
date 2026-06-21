def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_parts = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded_parts.append(f"{count}{current_char}")
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = run_length_encode(sample_input)
    print(result)