def sort_names(names):
    return sorted(set(names), key=lambda s: s.lower())

if __name__ == '__main__':
    sample_names = ["alice", "bob", "Charlie", "alice", "david", "Bob"]
    sorted_names = sort_names(sample_names)
    print(sorted_names)