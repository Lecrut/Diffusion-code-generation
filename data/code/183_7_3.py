def clean_names(line):
    return [name.strip() for name in line.split(':')]

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    print(clean_names(sample_line))