def group_by_length(items):
    categories = {}
    for item in items:
        length = len(item)
        if length not in categories:
            categories[length] = []
        categories[length].append(item)
    return {key: sorted(value) for key, value in categories.items()}

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    print(group_by_length(sample_items))