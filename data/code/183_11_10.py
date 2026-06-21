def clean_names(names):
    return [name.strip() for name in names if name.strip()]

def parse_line(line, delimiter=';'):
    split_names = line.split(delimiter)
    cleaned_names = clean_names(split_names)
    return cleaned_names
if __name__ == '__main__':
    sample_line = 'Eve; Frank ; Grace;;'
    result = parse_line(sample_line)
    print(result)