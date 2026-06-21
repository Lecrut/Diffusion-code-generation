def intersect_lists(names1, names2):
    if not all(isinstance(name, str) for name in names1 + names2):
        raise ValueError("Both lists must contain only strings.")
    
    lower_names1 = [name.lower() for name in names1]
    common_names = set(lower_names1).intersection(set(name.lower() for name in names2))
    return [name for name in names1 if name.lower() in common_names]

if __name__ == '__main__':
    sample_names1 = ["Alice", "Bob", "Charlie", "David", "Eve"]
    sample_names2 = ["alice", "bob", "Frank", "George"]
    result = intersect_lists(sample_names1, sample_names2)
    print(f"Common Names: {result}")