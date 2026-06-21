SEPARATOR = ';'

def parse_names(line):
    return [name.strip() for name in line.split(SEPARATOR) if name]

if __name__ == '__main__':
    sample_line = "Alice; Bob; Charlie; David"
    print(parse_names(sample_line))