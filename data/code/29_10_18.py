def encode_string(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = input_string[i]
            count = 1
            
    result.append(current_char)
    result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    encoded_result = encode_string(sample_input)
    print(encoded_result)