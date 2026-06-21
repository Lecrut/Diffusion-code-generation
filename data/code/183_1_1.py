def parse_names(line):
    return line.split(';')

if __name__ == '__main__':
    sample_line = "Alice;Bob;Charlie"
    print(parse_names(sample_line))