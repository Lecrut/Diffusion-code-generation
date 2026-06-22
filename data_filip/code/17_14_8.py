def run_length_encoding(input_string):
    if not input_string:
        return ""
    
    encoded_parts = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = input_string[i]
            count = 1
    
    encoded_parts.append(str(count) + current_char)
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_string = "aaabbbccccdd"
    result = run_length_encoding(sample_string)
    print(result)