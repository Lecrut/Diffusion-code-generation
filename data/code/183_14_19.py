def trim_names(names_str):
    return [name.strip() for name in names_str.split()]

if __name__ == '__main__':
    sample_names = "  Alice   Bob  Charlie  "
    trimmed_names = trim_names(sample_names)
    print(trimmed_names)