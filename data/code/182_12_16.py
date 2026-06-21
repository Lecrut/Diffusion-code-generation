def string_to_char_list(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    return list(input_string)
if __name__ == '__main__':
    sample_string_1 = 'hello'
    result_1 = string_to_char_list(sample_string_1)
    print(f'Input: {sample_string_1}')
    print(f'Separated Characters: {result_1}')
    sample_string_2 = 'world'
    result_2 = string_to_char_list(sample_string_2)
    print(f'Input: {sample_string_2}')
    print(f'Separated Characters: {result_2}')