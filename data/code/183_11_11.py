def parse_names(line):
    names = line.split(';')
    cleaned_names = [name.strip() for name in names if name.strip()]
    return cleaned_names

if __name__ == '__main__':
    sample_line = "John; Mary ; Paul;;"
    print(parse_names(sample_line))