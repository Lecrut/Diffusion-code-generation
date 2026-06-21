def run_length_encode(input_string):
    if not input_string:
        return {}
    
    encoded_dict = {}
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded_dict[current_char] = count
            current_char = char
            count = 1
            
    encoded_dict[current_char] = count
    
    return encoded_dict

if __name__ == '__main__':
    test_strings = [
        "AAABBBCC",
        "A",
        "ABABABAB",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBB",
        ""
    ]
    
    for test_str in test_strings:
        result = run_length_encode(test_str)
        print(result)