def group_by_length(items):
    groups = {}
    for item in items:
        length = len(item)
        if length not in groups:
            groups[length] = []
        groups[length].append(item)
    return {key: sorted(value) for key, value in groups.items()}

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date", "elderberry"]
    print(group_by_length(sample_items))