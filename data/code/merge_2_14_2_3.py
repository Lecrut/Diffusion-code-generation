def deduplicate_and_sort(arr):
    seen = set()
    distinct_items = []
    for item in arr:
        if isinstance(item, str) and (item not in seen):
            seen.add(item)
            distinct_items.append(item)
    return sorted(distinct_items)
if __name__ == '__main__':
    sample_data = ['banana', 'apple', 'cherry', 'date', 'elderberry'] +\
                  ['apple', 'fig']
    result = deduplicate_and_sort(sample_data)
    print(result)