INITIAL_CHAR = 'A'

def filter_names_by_initial(names):
    return [name for name in names if name.startswith(INITIAL_CHAR)]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    filtered_names = filter_names_by_initial(sample_names)
    print(filtered_names)