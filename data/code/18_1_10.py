def run_length_encode(input_string):
    if not input_string:
        return ""
    
    if len(input_string) == 1:
        return "1" + input_string
    
    result = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    text = "AAABBBCCD"
    encoded = run_length_encode(text)
    print(encoded)