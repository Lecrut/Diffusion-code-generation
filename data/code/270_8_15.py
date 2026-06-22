def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return input_string.replace(" ", "")

if __name__ == '__main__':
    sample_input = "This is a sample string with spaces"
    try:
        result = remove_spaces(sample_input)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")