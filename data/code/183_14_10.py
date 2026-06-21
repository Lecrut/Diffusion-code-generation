def trim_and_split_names(names_str):
    names_list = names_str.split()
    trimmed_names = [name.strip() for name in names_list]
    return trimmed_names

if __name__ == '__main__':
    sample_names = "  John   Doe  Jane Smith  "
    result = trim_and_split_names(sample_names)
    print(result)