def separate_and_clean_names(line):
    names = line.split(':')
    cleaned_names = [name.strip() for name in names]
    return cleaned_names

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    result = separate_and_clean_names(sample_line)
    print(result)