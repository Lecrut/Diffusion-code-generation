def remove_duplicates(names):
    seen = set()
    cleaned_names = []
    for name in names:
        if name not in seen:
            seen.add(name)
            cleaned_names.append(name)
    return cleaned_names

if __name__ == '__main__':
    sample_names1 = ["alice", "bob", "charlie", "david", "alice", "bob"]
    print("Original:", sample_names1)
    print("Cleaned:", remove_duplicates(sample_names1))