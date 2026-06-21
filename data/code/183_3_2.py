def extract_names(pipe_delimited_string):
    return pipe_delimited_string.split('|')

if __name__ == '__main__':
    sample_input = "Dave|Eve|Frank"
    names_list = extract_names(sample_input)
    print(names_list)