def run_length_encode(input_string):
    if not input_string:
        return []
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for index in range(1, len(input_string)):
        if input_string[index] == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = input_string[index]
            count = 1
    
    result.append((count, current_char))
    return result

if __name__ == '__main__':
    sample_data = "aaabbccccddeee"
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)