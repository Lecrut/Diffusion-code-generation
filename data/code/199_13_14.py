def filter_names(names, letter):
    return (name for name in names if name.startswith(letter))

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    filtered_names = list(filter_names(sample_names, 'A'))
    print(filtered_names)