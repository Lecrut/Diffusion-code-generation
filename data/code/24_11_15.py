def run_length_encode(input_str: str) -> str:
    if not input_str:
        return ""
    
    result = []
    count = 1
    current_char = input_str[0]
    
    for i in range(1, len(input_str)):
        char = input_str[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
            
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBC"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)