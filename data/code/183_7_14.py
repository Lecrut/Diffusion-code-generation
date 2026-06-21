def split_names(line):
    names = line.split(':')
    return [name.strip() for name in names if name]

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    result = split_names(sample_line)
    print(result)