def trim_and_split_names(names_str):
    return [name.strip() for name in names_str.split()]

if __name__ == '__main__':
    sample_names = "  Jane   Doe   Bob  Alice  "
    result = trim_and_split_names(sample_names)
    print(result)