def run_length_encode(input_string):
    if not input_string:
        return {}
    
    result = {}
    current_char = input_string[0]
    count = 1
    
    for index in range(1, len(input_string)):
        char = input_string[index]
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample_1 = "aaabbcccc"
    sample_2 = "a"
    sample_3 = "aaaa"
    sample_4 = ""
    
    print(run_length_encode(sample_1))
    print(run_length_encode(sample_2))
    print(run_length_encode(sample_3))
    print(run_length_encode(sample_4))