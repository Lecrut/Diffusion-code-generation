def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_chars = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(current_char)
            if count > 1:
                encoded_chars.append(str(count))
            current_char = char
            count = 1
    
    encoded_chars.append(current_char)
    if count > 1:
        encoded_chars.append(str(count))
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    result = run_length_encode('AAAABBBCCDAA')
    print(result)