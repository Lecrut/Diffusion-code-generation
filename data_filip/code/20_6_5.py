def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded_parts = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded_parts.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    
    encoded_parts.append(f"{count}{current_char}")
    
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_input = "AAABBBCCCCDDDEEEEFFFFGGG"
    result = run_length_encode(sample_input)
    print(result)
    
    sample_input_empty = ""
    result_empty = run_length_encode(sample_input_empty)
    print(result_empty)
    
    sample_input_single = "Z"
    result_single = run_length_encode(sample_input_single)
    print(result_single)
    
    sample_input_mixed = "112233344445"
    result_mixed = run_length_encode(sample_input_mixed)
    print(result_mixed)