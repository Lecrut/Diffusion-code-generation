def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    count = 0
    prev_char = input_string[0]
    
    for char in input_string:
        if char == prev_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{prev_char}")
            else:
                result.append(prev_char)
            count = 1
            prev_char = char
            
    if count > 1:
        result.append(f"{count}{prev_char}")
    else:
        result.append(prev_char)
        
    return "".join(result)

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAA"
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)