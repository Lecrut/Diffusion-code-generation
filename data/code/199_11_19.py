def remove_duplicates(names):
    seen = set()
    unique_names = []
    for name in names:
        if name not in seen:
            seen.add(name)
            unique_names.append(name)
    return unique_names

if __name__ == '__main__':
    sample_names2 = ["alice", "bob", "charlie", "david", "alice", "bob"]
    print("Original:", sample_names2)
    cleaned_names = remove_duplicates(sample_names2)
    print("Cleaned:", cleaned_names)