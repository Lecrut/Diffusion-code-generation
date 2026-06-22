def encode_string(input_str):
    if not input_str:
        return ""
    
    result = []
    current_char = input_str[0]
    count = 1
    
    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = input_str[i]
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccaaa"
    encoded_output = encode_string(sample_input)
    print(encoded_output)