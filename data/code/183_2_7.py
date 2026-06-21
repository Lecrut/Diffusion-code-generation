def split_names(names):
    if not isinstance(names, str):
        raise ValueError("Input must be a string")
    
    names_list = names.split()
    return [name for name in names_list if name]

if __name__ == '__main__':
    sample_names = "Alice Bob  Charlie   "
    print(split_names(sample_names))