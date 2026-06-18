def deduplicate_and_sort(items):
    seen = set()
    distinct_items = []
    for item in items:
        if isinstance(item, str) and not (item.startswith('"') and item.endswith('"')):
            normalized_item = item.strip().strip("'\"")
        else:
            normalized_item = item
        if normalized_item not in seen:
            seen.add(normalized_item)
            distinct_items.append(normalized_item)
    return sorted(distinct_items, key=str.lower)
if __name__ == '__main__':
    sample_data = ['banana', 'Apple', 'apple', "  Orange ", '"Banana"', 'cherry']
    result = deduplicate_and_sort(sample_data)
    print(result)