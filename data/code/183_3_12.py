def extract_names(pipe_delimited_string):
    return pipe_delimited_string.split('|')

if __name__ == '__main__':
    sample_string = "Alice|Bob|Charlie"
    print(extract_names(sample_string))