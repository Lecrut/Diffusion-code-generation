def separate_names(line):
    return [name.strip() for name in line.split(':')]

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    print(separate_names(sample_line))