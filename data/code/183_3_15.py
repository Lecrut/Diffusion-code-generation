def extract_names(pipe_delimited_string):
    names = pipe_delimited_string.split('|')
    return [name.strip() for name in names if name]

if __name__ == '__main__':
    sample_input = "  Mike|Lucy |George   |Zoe  "
    cleaned_names_list = extract_names(sample_input)
    print(cleaned_names_list)