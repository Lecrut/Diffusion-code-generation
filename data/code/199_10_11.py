def filter_long_names(names_list):
    long_names = [name for name in names_list if len(name) > 5]
    return long_names

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
    filtered_names = filter_long_names(sample_names)
    print(filtered_names)