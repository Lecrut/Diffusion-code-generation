def split_string_by_space(input_string):
    result = []
    current_word = []
    for char in input_string:
        if char == ' ':
            if current_word:
                result.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        result.append(''.join(current_word))
    return result

if __name__ == '__main__':
    sample_string_1 = "this is a sample string"
    result_1 = split_string_by_space(sample_string_1)
    print(f"Input: '{sample_string_1}'")
    print(f"Output: {result_1}")
    
    sample_string_2 = "  leading and trailing spaces   in between "
    result_2 = split_string_by_space(sample_string_2)
    print(f"Input: '{sample_string_2}'")
    print(f"Output: {result_2}")
    
    sample_string_3 = "singleword"
    result_3 = split_string_by_space(sample_string_3)
    print(f"Input: '{sample_string_3}'")
    print(f"Output: {result_3}")
    
    sample_string_4 = ""
    result_4 = split_string_by_space(sample_string_4)
    print(f"Input: '{sample_string_4}'")
    print(f"Output: {result_4}")