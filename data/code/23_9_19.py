def run_length_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    n = len(input_string)
    i = 0
    
    while i < n:
        current_char = input_string[i]
        count = 1
        i += 1
        
        while i < n and input_string[i] == current_char:
            count += 1
            i += 1
        
        result.append(str(count))
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDE"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)