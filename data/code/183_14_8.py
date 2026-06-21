def trim_and_split_names(names_str):
    if not isinstance(names_str, str) or not names_str.strip():
        raise ValueError("Input must be a non-empty string")
    
    return [name.strip() for name in names_str.split()]

if __name__ == '__main__':
    sample_names = "  Alice   Bob  Charlie  "
    print(trim_and_split_names(sample_names))