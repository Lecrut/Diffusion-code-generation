def run_length_encode(input_string):
    if not input_string:
        return []
    
    encoded = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    
    return encoded

if __name__ == '__main__':
    sample_string = 'AAAABBBCCDAA'
    result = run_length_encode(sample_string)
    print(result)