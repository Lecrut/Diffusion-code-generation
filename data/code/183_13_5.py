def pipe_to_list(names):
    if not isinstance(names, str) or '|' not in names:
        raise ValueError("Input must be a string containing at least one pipe character.")
    return [name.strip() for name in names.split('|') if name.strip()]

if __name__ == '__main__':
    sample_names = "Alice| Bob |Charlie||David"
    try:
        print(pipe_to_list(sample_names))
    except ValueError as e:
        print(e)