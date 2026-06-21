def validate_names(names):
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return [name for name in names if all(char in alphabet for char in name)]

def filter_alphabet_names(names):
    return [name for name in names if all(char.isalpha() for char in name)]

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'D@vid', 'Eve']
    filtered_names = filter_alphabet_names(sample_names)
    print(filtered_names)