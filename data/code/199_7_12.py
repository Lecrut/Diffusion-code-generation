def find_common_names(names1, names2):
    lower_names1 = {name.lower(): name for name in names1}
    common_names = [lower_names1.get(name.lower(), None) for name in names2 if name.lower() in lower_names1]
    return common_names

if __name__ == '__main__':
    sample_names1 = ["Alice", "Bob", "Charlie", "David", "Eve"]
    sample_names2 = ["alice", "bob", "Frank", "david"]
    result = find_common_names(sample_names1, sample_names2)
    print(f"Common Names: {result}")