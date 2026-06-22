def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    current_char = input_string[0]
    count = 1
    length = len(input_string)
    
    for i in range(1, length):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = char
            count = 1
    encoded.append(current_char + str(count))
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAA"
    result = run_length_encode(sample_input)
    print(result)