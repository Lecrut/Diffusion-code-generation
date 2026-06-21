def split_names(line):
    return line.split(':')

def strip_names(names):
    return [name.strip() for name in names]

def separate_and_clean(line):
    if not isinstance(line, str) or ':' not in line:
        raise ValueError("Input must be a colon-delimited string.")
    
    names = split_names(line)
    cleaned_names = strip_names(names)
    return cleaned_names

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    try:
        result = separate_and_clean(sample_line)
        print(result)
    except ValueError as e:
        print(e)