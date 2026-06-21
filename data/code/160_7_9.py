def filter_duplicates(item_names):
    seen = set()
    result = []
    for item in item_names:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    filtered_items = filter_duplicates(sample_items)
    print(filtered_items)