def filter_names_by_initial(names, initial):
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise ValueError("Names must be a list of strings")
    if not isinstance(initial, str) or len(initial) != 1:
        raise ValueError("Initial must be a single character string")
    
    return [name for name in names if name.startswith(initial)]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    initial_char = 'A'
    filtered_names = filter_names_by_initial(sample_names, initial_char)
    print(filtered_names)