def parse_names(line):
    return [name.strip() for name in line.split(';')]

if __name__ == '__main__':
    sample_line = "Alice; Bob; Charlie; David"
    result = parse_names(sample_line)
    print(result)