def remove_duplicates(names):
    seen = set()
    result = []
    for name in names:
        if name not in seen:
            seen.add(name)
            result.append(name)
    return result

if __name__ == '__main__':
    sample_names1 = ["alice", "bob", "charlie", "david", "alice"]
    cleaned_names = remove_duplicates(sample_names1)
    print("Cleaned:", cleaned_names)