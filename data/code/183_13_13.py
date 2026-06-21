PIPE_SEPARATOR = '|'

def pipe_to_list(names):
    return [name.strip() for name in names.split(PIPE_SEPARATOR) if name.strip()]

if __name__ == '__main__':
    sample_names = "Alice| Bob |Charlie||David"
    print(pipe_to_list(sample_names))