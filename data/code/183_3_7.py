def extract_names(pipe_delimited_string):
    if not isinstance(pipe_delimited_string, str) or '|' not in pipe_delimited_string:
        raise ValueError("Invalid input: Must be a non-empty string containing '|'")
    
    return [name.strip() for name in pipe_delimited_string.split('|')]

if __name__ == '__main__':
    sample_input = "Charlie|David|Eve"
    names_list = extract_names(sample_input)
    print(names_list)