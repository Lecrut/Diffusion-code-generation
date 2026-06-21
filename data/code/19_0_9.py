def run_length_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbbcccdd"
    encoded = run_length_encode(sample_string)
    print(encoded)