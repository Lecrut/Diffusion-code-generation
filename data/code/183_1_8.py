def parse_names(line):
    if not isinstance(line, str) or ';' not in line:
        raise ValueError("Invalid input: expected a semicolon-delimited string")
    return [name.strip() for name in line.split(';') if name]

if __name__ == '__main__':
    sample_line = "Alice; Bob; Charlie; David"
    try:
        print(parse_names(sample_line))
    except ValueError as e:
        print(e)