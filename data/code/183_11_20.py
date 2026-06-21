def parse_names(line):
    if not isinstance(line, str):
        raise ValueError("Input must be a string")
    names = line.split(';')
    cleaned_names = [name.strip() for name in names if name.strip()]
    return cleaned_names

if __name__ == '__main__':
    sample_line = "Eve; Frank ; Grace;;"
    print(parse_names(sample_line))