def clean_names(names):
    return [name.strip() for name in names if name.strip()]

def parse_line(line):
    return clean_names(line.split(';'))

if __name__ == '__main__':
    sample_line = "Eve; Frank ; Grace;;"
    print(parse_line(sample_line))