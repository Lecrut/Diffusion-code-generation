def is_valid_name(name):
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return all(char in alphabet for char in name)

def filter_names(names):
    if not isinstance(names, list) or not all(isinstance(item, str) for item in names):
        raise ValueError("Input must be a list of strings.")
    return [name for name in names if is_valid_name(name)]

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'D@vid', 'Eve']
    filtered_names = filter_names(sample_names)
    print(filtered_names)