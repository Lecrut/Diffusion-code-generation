def validate_input(input_string):
    if not isinstance(input_string, str) or '|' not in input_string:
        raise ValueError("Invalid input: must be a pipe-delimited string")

def extract_names(pipe_delimited_string):
    validate_input(pipe_delimited_string)
    return [name.strip() for name in pipe_delimited_string.split('|')]

if __name__ == '__main__':
    sample_input = "Alice|Bob|Charlie"
    names_list = extract_names(sample_input)
    print(names_list)