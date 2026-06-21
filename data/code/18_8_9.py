def encode_run_length(input_string):
    if not input_string:
        return []
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(count)
            current_char = char
            count = 1
    
    result.append(current_char)
    result.append(count)
    return result

if __name__ == '__main__':
    hardcoded_string = "AAABBBCCD"
    encoded = encode_run_length(hardcoded_string)
    print(encoded)