def parse_names(line):
    names = line.split(';')
    clean_names = [name.strip() for name in names if name.strip()]
    return clean_names

if __name__ == '__main__':
    sample_line = "Eve; Frank ; Grace;;"
    print(parse_names(sample_line))