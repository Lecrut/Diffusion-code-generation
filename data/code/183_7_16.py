def split_and_clean(line):
    return [name.strip() for name in line.split(':') if name.strip()]

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    cleaned_names = split_and_clean(sample_line)
    print(cleaned_names)