def separate_and_clean_names(line: str) -> list:
    return [name.strip() for name in line.split(':')]

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    result = separate_and_clean_names(sample_line)
    print(result)