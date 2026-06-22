def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded_parts = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded_parts.append(f"{count}{current_char}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "aaabbccccdddd"
    result = run_length_encode(sample_input)
    print(result)
    
    sample_input_2 = "WwwwwBbbBbb"
    result_2 = run_length_encode(sample_input_2)
    print(result_2)
    
    sample_input_3 = ""
    result_3 = run_length_encode(sample_input_3)
    print(result_3)