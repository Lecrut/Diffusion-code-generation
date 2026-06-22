def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_chars = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded_chars.append(str(count))
            encoded_chars.append(current_char)
            current_char = input_string[i]
            count = 1
    
    encoded_chars.append(str(count))
    encoded_chars.append(current_char)
    
    return ''.join(encoded_chars)

if __name__ == '__main__':
    data = "aabcccccaaa"
    result = run_length_encode(data)
    print(result)