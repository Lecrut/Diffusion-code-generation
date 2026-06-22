def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        current_char = s[i]
        count = 1
        while i + count < n and s[i + count] == current_char:
            count += 1
        result.append(f"{count}{current_char}")
        i += count
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcccc"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)
    
    empty_input = ""
    empty_output = run_length_encode(empty_input)
    print(empty_output)
    
    sample_input_2 = "xyz"
    encoded_output_2 = run_length_encode(sample_input_2)
    print(encoded_output_2)