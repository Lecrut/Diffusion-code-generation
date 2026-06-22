def run_length_encode(input_string):
    if not input_string:
        return {}
    
    result = {}
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = char
            count = 1
    
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample1 = "AAABBBCC"
    sample2 = "AABBCCCC"
    sample3 = "XYZ"
    sample4 = ""
    
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))