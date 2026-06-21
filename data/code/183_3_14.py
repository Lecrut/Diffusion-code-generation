def extract_names(pipe_delimited_string):
    SEPARATOR = '|'
    return pipe_delimited_string.split(SEPARATOR)

if __name__ == '__main__':
    sample_input = "Charlie|David|Eve"
    names_list = extract_names(sample_input)
    print(names_list)