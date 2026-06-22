def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccaaa"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)
    
    sample_input_two = "wwwwaaadexxxxxx"
    encoded_output_two = run_length_encode(sample_input_two)
    print(encoded_output_two)
    
    sample_input_three = ""
    encoded_output_three = run_length_encode(sample_input_three)
    print(encoded_output_three)