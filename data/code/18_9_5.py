def run_length_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    count = 1
    current_char = input_string[0]
    length = len(input_string)
    
    i = 1
    while i < length:
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = char
            count = 1
        i += 1
        
    result.append(current_char)
    result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbc"
    encoded = run_length_encode(sample_input)
    print(encoded)