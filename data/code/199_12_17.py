def sort_names(names):
    return sorted(names, key=str.lower)

if __name__ == '__main__':
    sample_names = ["alice", "bob", "Charlie", "alice", "david", "BOB"]
    sorted_list = sort_names(sample_names)
    print(sorted_list)