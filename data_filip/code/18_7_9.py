def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_parts = []
    count = 1
    length = len(input_string)
    current_char = input_string[0]
    
    for i in range(1, length):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(str(count))
            encoded_parts.append(current_char)
            current_char = char
            count = 1
    encoded_parts.append(str(count))
    encoded_parts.append(current_char)
    return "".join(encoded_parts)

if __name__ == '__main__':
    data = "aabcccccaaa"
    result = run_length_encode(data)
    print(result)