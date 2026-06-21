def parse_names(line):
    NAME_DELIMITER = ';'
    names = [name.strip() for name in line.split(NAME_DELIMITER) if name]
    return names

if __name__ == '__main__':
    sample_line = "Alice; Bob; Charlie; David"
    print(parse_names(sample_line))