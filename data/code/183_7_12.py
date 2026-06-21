NAMES_DELIMITER = ':'

def split_and_clean_names(line):
    return [name.strip() for name in line.split(NAMES_DELIMITER)]

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    result = split_and_clean_names(sample_line)
    print(result)