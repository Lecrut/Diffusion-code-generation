def run_length_encode(input_str):
    result = []
    if not input_str:
        return result
    
    current_char = input_str[0]
    count = 1
    
    for char in input_str[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    input_string = 'aabbaaccc'
    encoded_output = run_length_encode(input_string)
    print(encoded_output)