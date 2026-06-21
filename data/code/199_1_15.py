def filter_names_by_initial(names, initial):
    filtered = [name for name in names if name.startswith(initial)]
    return filtered

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    initial_char = 'A'
    result = filter_names_by_initial(sample_names, initial_char)
    print(result)