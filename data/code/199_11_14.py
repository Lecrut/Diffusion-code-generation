def remove_duplicates(names):
    seen = set()
    new_names = []
    for name in names:
        if name not in seen:
            seen.add(name)
            new_names.append(name)
    return new_names

if __name__ == '__main__':
    sample_names1 = ["alice", "bob", "charlie", "david", "alice"]
    print("Original:", sample_names1)
    cleaned_names = remove_duplicates(sample_names1)
    print("Cleaned:", cleaned_names)