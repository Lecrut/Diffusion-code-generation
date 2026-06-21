def process_names(names):
    unique_uppercased = set(name.upper() for name in names)
    sorted_descending = sorted(unique_uppercased, reverse=True)
    return sorted_descending

if __name__ == '__main__':
    sample_names = ["Alice", "bob", "Charlie", "alice", "Bob"]
    result = process_names(sample_names)
    print(result)