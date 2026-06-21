def convert_string_to_list(input_string):
    return list(input_string)

if __name__ == '__main__':
    sample_string_1 = "hello"
    result_1 = convert_string_to_list(sample_string_1)
    print(f"Input: {sample_string_1}")
    print(f"Characters as List: {result_1}")
    
    sample_string_2 = "world"
    result_2 = convert_string_to_list(sample_string_2)
    print(f"Input: {sample_string_2}")
    print(f"Characters as List: {result_2}")