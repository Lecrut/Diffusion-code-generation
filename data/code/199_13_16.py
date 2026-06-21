def filter_names(names, start_letter):
    return (name for name in names if name.startswith(start_letter))

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    filtered_names = filter_names(sample_names, 'A')
    print(list(filtered_names))