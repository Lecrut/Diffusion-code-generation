def filter_names_by_initial(names, initial):
    INITIAL_CHAR = initial.upper()
    return [name for name in names if name.startswith(INITIAL_CHAR)]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    initial_char = 'A'
    filtered_names = filter_names_by_initial(sample_names, initial_char)
    print(filtered_names)