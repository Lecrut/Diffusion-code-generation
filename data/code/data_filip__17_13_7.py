def run_length_encode(text):
    if not text:
        return ""
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    result = run_length_encode(sample_input)
    print(result)
    
    sample_input_2 = "A"
    result_2 = run_length_encode(sample_input_2)
    print(result_2)
    
    sample_input_3 = "AABBCC"
    result_3 = run_length_encode(sample_input_3)
    print(result_3)