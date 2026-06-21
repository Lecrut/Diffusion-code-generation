SORT_KEY = lambda name: name.lower()

if __name__ == '__main__':
    sample_names = ["alice", "bob", "Charlie", "alice", "david", "Bob"]
    sorted_names = sorted(sample_names, key=SORT_KEY)
    print(sorted_names)