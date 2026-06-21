def filter_names_by_initial(names, initial):
    return [name for name in names if name.startswith(initial.upper())]

if __name__ == '__main__':
    SAMPLE_NAMES = ["Alice", "Bob", "Charlie", "Diana"]
    INITIAL_CHAR = 'A'
    filtered_names = filter_names_by_initial(SAMPLE_NAMES, INITIAL_CHAR)
    print(filtered_names)