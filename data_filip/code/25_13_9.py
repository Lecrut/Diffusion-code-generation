def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    count = 1
    char = input_string[0]
    
    for i in range(1, len(input_string)):
        current_char = input_string[i]
        if current_char == char:
            count += 1
        else:
            result.append(f"{count}{char}")
            char = current_char
            count = 1
            
    result.append(f"{count}{char}")
    
    return "".join(result)

def run_length_decode(encoded_string: str) -> str:
    if not encoded_string:
        return ""
    
    result = []
    i = 0
    n = len(encoded_string)
    
    while i < n:
        count_str = []
        while i < n and encoded_string[i].isdigit():
            count_str.append(encoded_string[i])
            i += 1
        
        count = int("".join(count_str))
        
        if i < n:
            char = encoded_string[i]
            i += 1
            result.append(char * count)
            
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)
    
    decoded_output = run_length_decode(encoded_output)
    print(decoded_output)
    
    sample_input_2 = "abc"
    encoded_output_2 = run_length_encode(sample_input_2)
    print(encoded_output_2)
    
    sample_input_3 = ""
    encoded_output_3 = run_length_encode(sample_input_3)
    print(repr(encoded_output_3))