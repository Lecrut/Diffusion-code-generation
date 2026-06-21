def sort_names(names):
    processed_names = [name.lower() for name in names]
    processed_names.sort()
    return processed_names

if __name__ == '__main__':
    sample_names = ["Alice", "bob", "Charlie", "alice", "David", "BOB"]
    sorted_list = sort_names(sample_names)
    print(sorted_list)