def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def separate_string_to_list_of_characters(input_string):
    validate_input(input_string)
    return list(input_string)

if __name__ == '__main__':
    sample_string = "Hello World"
    result = separate_string_to_list_of_characters(sample_string)
    print(result)