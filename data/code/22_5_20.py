def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccdddeee"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    
    sample_input_two = "aabbcc"
    encoded_result_two = run_length_encode(sample_input_two)
    print(encoded_result_two)
    
    sample_input_three = "zzzzzzzzzz"
    encoded_result_three = run_length_encode(sample_input_three)
    print(encoded_result_three)
    
    sample_input_four = ""
    encoded_result_four = run_length_encode(sample_input_four)
    print(encoded_result_four)