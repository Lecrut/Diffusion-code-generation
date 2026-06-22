def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
            
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbc"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    sample_input_2 = "aA1!bB2@"
    encoded_result_2 = run_length_encode(sample_input_2)
    print(encoded_result_2)
    
    sample_input_3 = "aaaa"
    encoded_result_3 = run_length_encode(sample_input_3)
    print(encoded_result_3)
    
    sample_input_4 = ""
    encoded_result_4 = run_length_encode(sample_input_4)
    print(encoded_result_4)