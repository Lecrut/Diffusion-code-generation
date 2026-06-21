def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_chars = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(current_char + str(count))
            current_char = char
            count = 1
    
    encoded_chars.append(current_char + str(count))
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_string = "AAABBC"
    result = run_length_encode(sample_string)
    print(result)