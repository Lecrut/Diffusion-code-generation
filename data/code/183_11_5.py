def parse_names(line):
    return [name.strip() for name in line.split(';') if name.strip()]

if __name__ == '__main__':
    sample_line = "Alice; Bob ; Charlie;;"
    print(parse_names(sample_line))