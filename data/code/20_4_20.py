def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    prev_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        current_char = input_string[i]
        if current_char == prev_char:
            count += 1
        else:
            result.append(f"{count}{prev_char}")
            prev_char = current_char
            count = 1
    
    result.append(f"{count}{prev_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AABBBCCCC"
    encoded_value = run_length_encode(sample_string)
    print(encoded_value)