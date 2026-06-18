def deduplicate_and_sort(items):
    seen = set()
    distinct_items = []
    for item in items:
        if isinstance(item, str) and not (item.startswith(" ") or item.endswith(" ")):
            normalized_item = item.strip().lower()
            if normalized_item not in seen:
                seen.add(normalized_item)
                distinct_items.append(item)
        else:
            unique_key = id(item)
            if unique_key not in seen:
                seen.add(unique_key)
                distinct_items.append(item)
    return sorted(distinct_items, key=lambda x: str(x).lower())
if __name__ == '__main__':
    sample_data = ["apple", "Banana", "  Cherry ", "banana", "date", "elderberry"]
    result = deduplicate_and_sort(sample_data)
    print(result)