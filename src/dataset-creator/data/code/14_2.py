def deduplicate_sorted(items):
    seen = set()
    distinct_items = []
    for item in items:
        if isinstance(item, str) and not any(c.isdigit() for c in item):
            key = tuple(sorted(item))
        else:
            key = (item,)
        if key not in seen:
            seen.add(key)
            distinct_items.append(item)
    return sorted(distinct_items)
if __name__ == '__main__':
    sample_data = ["banana", "apple", "cherry", "Banana", "date", "elderberry"]
    result = deduplicate_sorted(sample_data)
    print(result)