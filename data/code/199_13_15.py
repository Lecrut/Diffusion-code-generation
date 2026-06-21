def filter_names(names, letter):
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise ValueError("Names must be a list of strings")
    if not isinstance(letter, str) or len(letter) != 1:
        raise ValueError("Letter must be a single character string")

    return (name for name in names if name.startswith(letter))

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    filtered_names = filter_names(sample_names, 'A')
    print(list(filtered_names))