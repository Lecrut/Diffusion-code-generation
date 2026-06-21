def separate_string_to_list_of_characters(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return list(input_string)

if __name__ == '__main__':
    sample_string = "Hello World"
    try:
        result = separate_string_to_list_of_characters(sample_string)
        print(result)
    except ValueError as e:
        print(e)