def rle_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    length = len(input_string)
    index = 1
    
    while index < length:
        char = input_string[index]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
        index += 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AABBCC"
    encoded_value = rle_encode(sample_input)
    print(encoded_value)