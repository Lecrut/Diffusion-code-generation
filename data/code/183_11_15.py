def parse_names(line):
    if not isinstance(line, str) or ';' not in line:
        raise ValueError("Invalid input: Expected a string containing semicolons.")
    
    names = [name.strip() for name in line.split(';') if name.strip()]
    return names

if __name__ == '__main__':
    sample_line = "Eve; Frank ; Grace;;"
    print(parse_names(sample_line))