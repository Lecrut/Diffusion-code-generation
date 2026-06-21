def extract_names(pipe_delimited_string):
    if not isinstance(pipe_delimited_string, str) or '|' not in pipe_delimited_string:
        raise ValueError("Invalid input: must be a non-empty string containing '|'")
    return [name.strip() for name in pipe_delimited_string.split('|') if name.strip()]

if __name__ == '__main__':
    sample_input = "  Alice | Bob   | Charlie  "
    names_list = extract_names(sample_input)
    print(names_list)