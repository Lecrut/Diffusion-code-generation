def clean_names(line):
    if not isinstance(line, str) or ':' not in line:
        raise ValueError("Input must be a colon-delimited string")
    names = [name.strip() for name in line.split(':')]
    return names

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    try:
        result = clean_names(sample_line)
        print(result)
    except ValueError as e:
        print(e)