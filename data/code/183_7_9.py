def separate_and_clean_names(line):
    if not isinstance(line, str) or ':' not in line:
        raise ValueError("Input must be a string containing at least one colon.")
    
    names = line.split(':')
    cleaned_names = [name.strip() for name in names]
    return cleaned_names

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    try:
        result = separate_and_clean_names(sample_line)
        print(result)
    except ValueError as e:
        print(e)