def split_names(names):
    if not isinstance(names, str) or len(names.strip()) == 0:
        raise ValueError("Input must be a non-empty string of names separated by spaces.")
    
    return [name for name in names.split() if name]

if __name__ == '__main__':
    sample_names = "Alice Bob  Charlie   "
    print(split_names(sample_names))