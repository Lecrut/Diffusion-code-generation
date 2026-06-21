def filter_names_by_length(names):
    return [name for name in names if len(name) > 5]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "alice", "Bob"]
    filtered_names = filter_names_by_length(sample_names)
    print(filtered_names)