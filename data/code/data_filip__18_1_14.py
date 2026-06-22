def run_length_encode(input_string):
    if not input_string:
        return ""
    
    if len(input_string) == 1:
        return "1" + input_string
    
    encoded = ""
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded += str(count)
            encoded += current_char
            current_char = char
            count = 1
    
    if count > 1:
        encoded += str(count)
    encoded += current_char
    
    return encoded

if __name__ == '__main__':
    text = "aaabbbcccaaa"
    result = run_length_encode(text)
    print(result)