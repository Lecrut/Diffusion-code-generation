NAMES_SEPARATOR = ' '

def trim_and_split_names(names_str):
    return [name.strip() for name in names_str.split(NAMES_SEPARATOR)]

if __name__ == '__main__':
    sample_names = "  Alice   Bob  Charlie  "
    print(trim_and_split_names(sample_names))