def filter_long_names(names_list):
    if not isinstance(names_list, list) or not all(isinstance(name, str) for name in names_list):
        raise ValueError("Input must be a list of strings")
    
    return [name for name in names_list if len(name) > 5]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "alice", "Bob"]
    result = filter_long_names(sample_names)
    print(result)