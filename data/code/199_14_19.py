def merge_and_uniq_sort(names1, names2):
    merged = names1 + names2
    cleaned = [name.strip() for name in merged if name.strip()]
    unique = list(set(cleaned))
    return sorted(unique)

if __name__ == '__main__':
    sample_names1 = ["Alice", "Bob", " Charlie"]
    sample_names2 = ["David ", "Eve", "Charlie"]
    result = merge_and_uniq_sort(sample_names1, sample_names2)
    print(result)