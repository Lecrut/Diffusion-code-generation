def run_length_encode(input_str):
    if not input_str:
        return ""
    
    result = []
    count = 1
    prev_char = input_str[0]
    
    for i in range(1, len(input_str)):
        char = input_str[i]
        if char == prev_char:
            count += 1
        else:
            result.append(f"{count}{prev_char}")
            count = 1
            prev_char = char
    
    result.append(f"{count}{prev_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAA"
    encoded = run_length_encode(sample_input)
    print(encoded)