def group_by_length(items):
    result = {}
    for item in items:
        length = len(item)
        if length not in result:
            result[length] = []
        result[length].append(item)
    return {k: sorted(v) for k, v in result.items()}

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date", "elderberry"]
    grouped_items = group_by_length(sample_items)
    print(grouped_items)