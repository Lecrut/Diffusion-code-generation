def run_length_encode(text):
    if not text:
        return ""
    
    result = []
    n = len(text)
    i = 0
    
    while i < n:
        count = 1
        current_char = text[i]
        i += 1
        
        while i < n and text[i] == current_char:
            count += 1
            i += 1
        
        result.append(current_char)
        result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccdd"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)
    
    sample_input_empty = ""
    encoded_output_empty = run_length_encode(sample_input_empty)
    print(encoded_output_empty)
    
    sample_input_single = "a"
    encoded_output_single = run_length_encode(sample_input_single)
    print(encoded_output_single)
    
    sample_input_mixed = "aabbccc"
    encoded_output_mixed = run_length_encode(sample_input_mixed)
    print(encoded_output_mixed)