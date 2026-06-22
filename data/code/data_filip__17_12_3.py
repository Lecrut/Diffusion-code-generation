def run_length_encode_alphanumeric(input_string):
    if not input_string:
        return {}
    
    result = {}
    i = 0
    length = len(input_string)
    
    while i < length:
        if not input_string[i].isalnum():
            i += 1
            continue
        
        current_char = input_string[i]
        count = 0
        
        while i < length and input_string[i] == current_char:
            count += 1
            i += 1
        
        result[current_char] = count
    
    return result

if __name__ == '__main__':
    sample_input = "aaabb333ccc1"
    encoded_result = run_length_encode_alphanumeric(sample_input)
    print(encoded_result)