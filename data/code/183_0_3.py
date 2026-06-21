def process_names(names_str):
    names_list = names_str.split(',')
    stripped_names = [name.strip() for name in names_list]
    return stripped_names

if __name__ == '__main__':
    sample_names = "  Eve, Frank ,Grace, Henry   "
    result = process_names(sample_names)
    print(result)